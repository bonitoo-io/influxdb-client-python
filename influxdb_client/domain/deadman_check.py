# coding: utf-8

"""
Influx OSS API Service.

No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

OpenAPI spec version: 2.0.0
Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six
from influxdb_client.domain.check_discriminator import CheckDiscriminator


class DeadmanCheck(CheckDiscriminator):
    """NOTE: This class is auto generated by OpenAPI Generator.

    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'type': 'str',
        'time_since': 'str',
        'stale_time': 'str',
        'report_zero': 'bool',
        'level': 'CheckStatusLevel',
        'every': 'str',
        'offset': 'str',
        'tags': 'list[object]',
        'status_message_template': 'str',
        'id': 'str',
        'name': 'str',
        'org_id': 'str',
        'task_id': 'str',
        'owner_id': 'str',
        'created_at': 'datetime',
        'updated_at': 'datetime',
        'query': 'DashboardQuery',
        'status': 'TaskStatusType',
        'description': 'str',
        'latest_completed': 'datetime',
        'last_run_status': 'str',
        'last_run_error': 'str',
        'labels': 'list[Label]',
        'links': 'CheckBaseLinks'
    }

    attribute_map = {
        'type': 'type',
        'time_since': 'timeSince',
        'stale_time': 'staleTime',
        'report_zero': 'reportZero',
        'level': 'level',
        'every': 'every',
        'offset': 'offset',
        'tags': 'tags',
        'status_message_template': 'statusMessageTemplate',
        'id': 'id',
        'name': 'name',
        'org_id': 'orgID',
        'task_id': 'taskID',
        'owner_id': 'ownerID',
        'created_at': 'createdAt',
        'updated_at': 'updatedAt',
        'query': 'query',
        'status': 'status',
        'description': 'description',
        'latest_completed': 'latestCompleted',
        'last_run_status': 'lastRunStatus',
        'last_run_error': 'lastRunError',
        'labels': 'labels',
        'links': 'links'
    }

    def __init__(self, type="deadman", time_since=None, stale_time=None, report_zero=None, level=None, every=None, offset=None, tags=None, status_message_template=None, id=None, name=None, org_id=None, task_id=None, owner_id=None, created_at=None, updated_at=None, query=None, status=None, description=None, latest_completed=None, last_run_status=None, last_run_error=None, labels=None, links=None):  # noqa: E501,D401,D403
        """DeadmanCheck - a model defined in OpenAPI."""  # noqa: E501
        CheckDiscriminator.__init__(self, id=id, name=name, org_id=org_id, task_id=task_id, owner_id=owner_id, created_at=created_at, updated_at=updated_at, query=query, status=status, description=description, latest_completed=latest_completed, last_run_status=last_run_status, last_run_error=last_run_error, labels=labels, links=links)  # noqa: E501

        self._type = None
        self._time_since = None
        self._stale_time = None
        self._report_zero = None
        self._level = None
        self._every = None
        self._offset = None
        self._tags = None
        self._status_message_template = None
        self.discriminator = None

        self.type = type
        if time_since is not None:
            self.time_since = time_since
        if stale_time is not None:
            self.stale_time = stale_time
        if report_zero is not None:
            self.report_zero = report_zero
        if level is not None:
            self.level = level
        if every is not None:
            self.every = every
        if offset is not None:
            self.offset = offset
        if tags is not None:
            self.tags = tags
        if status_message_template is not None:
            self.status_message_template = status_message_template

    @property
    def type(self):
        """Get the type of this DeadmanCheck.

        :return: The type of this DeadmanCheck.
        :rtype: str
        """  # noqa: E501
        return self._type

    @type.setter
    def type(self, type):
        """Set the type of this DeadmanCheck.

        :param type: The type of this DeadmanCheck.
        :type: str
        """  # noqa: E501
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        self._type = type

    @property
    def time_since(self):
        """Get the time_since of this DeadmanCheck.

        String duration before deadman triggers.

        :return: The time_since of this DeadmanCheck.
        :rtype: str
        """  # noqa: E501
        return self._time_since

    @time_since.setter
    def time_since(self, time_since):
        """Set the time_since of this DeadmanCheck.

        String duration before deadman triggers.

        :param time_since: The time_since of this DeadmanCheck.
        :type: str
        """  # noqa: E501
        self._time_since = time_since

    @property
    def stale_time(self):
        """Get the stale_time of this DeadmanCheck.

        String duration for time that a series is considered stale and should not trigger deadman.

        :return: The stale_time of this DeadmanCheck.
        :rtype: str
        """  # noqa: E501
        return self._stale_time

    @stale_time.setter
    def stale_time(self, stale_time):
        """Set the stale_time of this DeadmanCheck.

        String duration for time that a series is considered stale and should not trigger deadman.

        :param stale_time: The stale_time of this DeadmanCheck.
        :type: str
        """  # noqa: E501
        self._stale_time = stale_time

    @property
    def report_zero(self):
        """Get the report_zero of this DeadmanCheck.

        If only zero values reported since time, trigger an alert

        :return: The report_zero of this DeadmanCheck.
        :rtype: bool
        """  # noqa: E501
        return self._report_zero

    @report_zero.setter
    def report_zero(self, report_zero):
        """Set the report_zero of this DeadmanCheck.

        If only zero values reported since time, trigger an alert

        :param report_zero: The report_zero of this DeadmanCheck.
        :type: bool
        """  # noqa: E501
        self._report_zero = report_zero

    @property
    def level(self):
        """Get the level of this DeadmanCheck.

        :return: The level of this DeadmanCheck.
        :rtype: CheckStatusLevel
        """  # noqa: E501
        return self._level

    @level.setter
    def level(self, level):
        """Set the level of this DeadmanCheck.

        :param level: The level of this DeadmanCheck.
        :type: CheckStatusLevel
        """  # noqa: E501
        self._level = level

    @property
    def every(self):
        """Get the every of this DeadmanCheck.

        Check repetition interval.

        :return: The every of this DeadmanCheck.
        :rtype: str
        """  # noqa: E501
        return self._every

    @every.setter
    def every(self, every):
        """Set the every of this DeadmanCheck.

        Check repetition interval.

        :param every: The every of this DeadmanCheck.
        :type: str
        """  # noqa: E501
        self._every = every

    @property
    def offset(self):
        """Get the offset of this DeadmanCheck.

        Duration to delay after the schedule, before executing check.

        :return: The offset of this DeadmanCheck.
        :rtype: str
        """  # noqa: E501
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Set the offset of this DeadmanCheck.

        Duration to delay after the schedule, before executing check.

        :param offset: The offset of this DeadmanCheck.
        :type: str
        """  # noqa: E501
        self._offset = offset

    @property
    def tags(self):
        """Get the tags of this DeadmanCheck.

        List of tags to write to each status.

        :return: The tags of this DeadmanCheck.
        :rtype: list[object]
        """  # noqa: E501
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Set the tags of this DeadmanCheck.

        List of tags to write to each status.

        :param tags: The tags of this DeadmanCheck.
        :type: list[object]
        """  # noqa: E501
        self._tags = tags

    @property
    def status_message_template(self):
        """Get the status_message_template of this DeadmanCheck.

        The template used to generate and write a status message.

        :return: The status_message_template of this DeadmanCheck.
        :rtype: str
        """  # noqa: E501
        return self._status_message_template

    @status_message_template.setter
    def status_message_template(self, status_message_template):
        """Set the status_message_template of this DeadmanCheck.

        The template used to generate and write a status message.

        :param status_message_template: The status_message_template of this DeadmanCheck.
        :type: str
        """  # noqa: E501
        self._status_message_template = status_message_template

    def to_dict(self):
        """Return the model properties as a dict."""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Return the string representation of the model."""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`."""
        return self.to_str()

    def __eq__(self, other):
        """Return true if both objects are equal."""
        if not isinstance(other, DeadmanCheck):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return true if both objects are not equal."""
        return not self == other
