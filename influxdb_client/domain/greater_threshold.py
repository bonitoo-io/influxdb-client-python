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
from influxdb_client.domain.threshold import Threshold


class GreaterThreshold(Threshold):
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
        'value': 'float',
        'level': 'CheckStatusLevel',
        'all_values': 'bool'
    }

    attribute_map = {
        'type': 'type',
        'value': 'value',
        'level': 'level',
        'all_values': 'allValues'
    }

    def __init__(self, type="greater", value=None, level=None, all_values=None):  # noqa: E501,D401,D403
        """GreaterThreshold - a model defined in OpenAPI."""  # noqa: E501
        Threshold.__init__(self, level=level, all_values=all_values)  # noqa: E501

        self._type = None
        self._value = None
        self.discriminator = None

        self.type = type
        self.value = value

    @property
    def type(self):
        """Get the type of this GreaterThreshold.

        :return: The type of this GreaterThreshold.
        :rtype: str
        """  # noqa: E501
        return self._type

    @type.setter
    def type(self, type):
        """Set the type of this GreaterThreshold.

        :param type: The type of this GreaterThreshold.
        :type: str
        """  # noqa: E501
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        self._type = type

    @property
    def value(self):
        """Get the value of this GreaterThreshold.

        :return: The value of this GreaterThreshold.
        :rtype: float
        """  # noqa: E501
        return self._value

    @value.setter
    def value(self, value):
        """Set the value of this GreaterThreshold.

        :param value: The value of this GreaterThreshold.
        :type: float
        """  # noqa: E501
        if value is None:
            raise ValueError("Invalid value for `value`, must not be `None`")  # noqa: E501
        self._value = value

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
        if not isinstance(other, GreaterThreshold):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return true if both objects are not equal."""
        return not self == other
