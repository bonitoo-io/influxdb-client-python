"""Implementation for Retry strategy during HTTP requests."""

import logging
from datetime import datetime, timedelta
from itertools import takewhile
from random import random

from urllib3 import Retry
from urllib3.exceptions import MaxRetryError, ResponseError

from influxdb_client.client.exceptions import InfluxDBError

logger = logging.getLogger(__name__)


class WritesRetry(Retry):
    """
    Writes retry configuration.

    :param int max_retry_time: maximum total retry timout in seconds, attempt after this timout throws MaxRetryError
    :param int total: maximum number of retries
    :param num backoff_factor: initial first retry delay range in seconds
    :param num max_retry_delay: maximum delay when retrying write in seconds
    :param num min_retry_delay: minimum delay when retrying write in seconds
    :param int exponential_base: base for the exponential retry delay, the next delay is computed as
                                 `backoff_factor * exponential_base^(attempts-1) * random()`
    """

    def __init__(self, max_retry_time=180, total=10, backoff_factor=5, max_retry_delay=125, min_retry_delay=1,
                 exponential_base=2, **kw):
        """Initialize defaults."""
        super().__init__(**kw)
        self.total = total
        self.backoff_factor = backoff_factor
        self.max_retry_delay = max_retry_delay
        self.min_retry_delay = min_retry_delay
        self.max_retry_time = max_retry_time
        self.exponential_base = exponential_base
        self.retry_timeout = datetime.now() + timedelta(seconds=max_retry_time)

    def new(self, **kw):
        """Initialize defaults."""
        if 'max_retry_delay' not in kw:
            kw['max_retry_delay'] = self.max_retry_delay

        if 'min_retry_delay' not in kw:
            kw['min_retry_delay'] = self.min_retry_delay

        if 'max_retry_time' not in kw:
            kw['max_retry_time'] = self.max_retry_time

        if 'exponential_base' not in kw:
            kw['exponential_base'] = self.exponential_base

        new = super().new(**kw)
        new.retry_timeout = self.retry_timeout
        return new

    def is_retry(self, method, status_code, has_retry_after=False):
        """is_retry doesn't require retry_after header. If there is not Retry-After we will use backoff."""
        if not self._is_method_retryable(method):
            return False

        return self.total and (status_code >= 429)

    def get_backoff_time(self):
        """Variant of exponential backoff with initial and max delay and a random jitter delay."""
        # We want to consider only the last consecutive errors sequence (Ignore redirects).
        consecutive_errors_len = len(
            list(
                takewhile(lambda x: x.redirect_location is None, reversed(self.history))
            )
        )
        # First fail doesn't increase backoff
        consecutive_errors_len -= 1
        if consecutive_errors_len < 0:
            return 0

        delay_range = self.backoff_factor
        i = 1
        while i <= consecutive_errors_len:
            i += 1
            delay_range = delay_range * self.exponential_base
            if delay_range > self.max_retry_delay:
                break

        delay = self.min_retry_delay + (delay_range - self.min_retry_delay) * self._random()
        # at least min_retry_delay
        delay = max(self.min_retry_delay, delay)
        # at most max_retry_delay
        delay = min(self.max_retry_delay, delay)
        return delay

    def increment(self, method=None, url=None, response=None, error=None, _pool=None, _stacktrace=None):
        """Return a new Retry object with incremented retry counters."""
        if self.retry_timeout < datetime.now():
            raise MaxRetryError(_pool, url, error or ResponseError("max_retry_time exceeded"))

        new_retry = super().increment(method, url, response, error, _pool, _stacktrace)

        if response is not None:
            parsed_error = InfluxDBError(response=response)
        elif error is not None:
            parsed_error = error
        else:
            parsed_error = f"Failed request to: {url}"

        message = f"The retriable error occurred during request. Reason: '{parsed_error}'."
        if isinstance(parsed_error, InfluxDBError):
            message += f" Retry in {parsed_error.retry_after}s."

        logger.warning(message)

        return new_retry

    def _random(self):
        return random()
