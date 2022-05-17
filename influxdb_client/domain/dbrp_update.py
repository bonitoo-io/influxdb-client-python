# coding: utf-8

"""
InfluxDB OSS API Service.

The InfluxDB v2 API provides a programmatic interface for all interactions with InfluxDB. Access the InfluxDB API using the `/api/v2/` endpoint.   # noqa: E501

OpenAPI spec version: 2.0.0
Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401


class DBRPUpdate(object):
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
        'retention_policy': 'str',
        'default': 'bool'
    }

    attribute_map = {
        'retention_policy': 'retention_policy',
        'default': 'default'
    }

    def __init__(self, retention_policy=None, default=None):  # noqa: E501,D401,D403
        """DBRPUpdate - a model defined in OpenAPI."""  # noqa: E501
        self._retention_policy = None
        self._default = None
        self.discriminator = None

        if retention_policy is not None:
            self.retention_policy = retention_policy
        if default is not None:
            self.default = default

    @property
    def retention_policy(self):
        """Get the retention_policy of this DBRPUpdate.

        InfluxDB v1 retention policy

        :return: The retention_policy of this DBRPUpdate.
        :rtype: str
        """  # noqa: E501
        return self._retention_policy

    @retention_policy.setter
    def retention_policy(self, retention_policy):
        """Set the retention_policy of this DBRPUpdate.

        InfluxDB v1 retention policy

        :param retention_policy: The retention_policy of this DBRPUpdate.
        :type: str
        """  # noqa: E501
        self._retention_policy = retention_policy

    @property
    def default(self):
        """Get the default of this DBRPUpdate.

        :return: The default of this DBRPUpdate.
        :rtype: bool
        """  # noqa: E501
        return self._default

    @default.setter
    def default(self, default):
        """Set the default of this DBRPUpdate.

        :param default: The default of this DBRPUpdate.
        :type: bool
        """  # noqa: E501
        self._default = default

    def to_dict(self):
        """Return the model properties as a dict."""
        result = {}

        for attr, _ in self.openapi_types.items():
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
        if not isinstance(other, DBRPUpdate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return true if both objects are not equal."""
        return not self == other
