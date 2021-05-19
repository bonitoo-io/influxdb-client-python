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


class AuthorizationUpdateRequest(object):
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
        'status': 'str',
        'description': 'str'
    }

    attribute_map = {
        'status': 'status',
        'description': 'description'
    }

    def __init__(self, status='active', description=None):  # noqa: E501,D401,D403
        """AuthorizationUpdateRequest - a model defined in OpenAPI."""  # noqa: E501
        self._status = None
        self._description = None
        self.discriminator = None

        if status is not None:
            self.status = status
        if description is not None:
            self.description = description

    @property
    def status(self):
        """Get the status of this AuthorizationUpdateRequest.

        If inactive the token is inactive and requests using the token will be rejected.

        :return: The status of this AuthorizationUpdateRequest.
        :rtype: str
        """  # noqa: E501
        return self._status

    @status.setter
    def status(self, status):
        """Set the status of this AuthorizationUpdateRequest.

        If inactive the token is inactive and requests using the token will be rejected.

        :param status: The status of this AuthorizationUpdateRequest.
        :type: str
        """  # noqa: E501
        self._status = status

    @property
    def description(self):
        """Get the description of this AuthorizationUpdateRequest.

        A description of the token.

        :return: The description of this AuthorizationUpdateRequest.
        :rtype: str
        """  # noqa: E501
        return self._description

    @description.setter
    def description(self, description):
        """Set the description of this AuthorizationUpdateRequest.

        A description of the token.

        :param description: The description of this AuthorizationUpdateRequest.
        :type: str
        """  # noqa: E501
        self._description = description

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
        if not isinstance(other, AuthorizationUpdateRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return true if both objects are not equal."""
        return not self == other
