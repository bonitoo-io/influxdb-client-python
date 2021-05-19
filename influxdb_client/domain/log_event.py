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


class LogEvent(object):
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
        'time': 'datetime',
        'message': 'str'
    }

    attribute_map = {
        'time': 'time',
        'message': 'message'
    }

    def __init__(self, time=None, message=None):  # noqa: E501,D401,D403
        """LogEvent - a model defined in OpenAPI."""  # noqa: E501
        self._time = None
        self._message = None
        self.discriminator = None

        if time is not None:
            self.time = time
        if message is not None:
            self.message = message

    @property
    def time(self):
        """Get the time of this LogEvent.

        Time event occurred, RFC3339Nano.

        :return: The time of this LogEvent.
        :rtype: datetime
        """  # noqa: E501
        return self._time

    @time.setter
    def time(self, time):
        """Set the time of this LogEvent.

        Time event occurred, RFC3339Nano.

        :param time: The time of this LogEvent.
        :type: datetime
        """  # noqa: E501
        self._time = time

    @property
    def message(self):
        """Get the message of this LogEvent.

        A description of the event that occurred.

        :return: The message of this LogEvent.
        :rtype: str
        """  # noqa: E501
        return self._message

    @message.setter
    def message(self, message):
        """Set the message of this LogEvent.

        A description of the event that occurred.

        :param message: The message of this LogEvent.
        :type: str
        """  # noqa: E501
        self._message = message

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
        if not isinstance(other, LogEvent):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return true if both objects are not equal."""
        return not self == other
