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
from influxdb_client.domain.statement import Statement


class VariableAssignment(Statement):
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
        'id': 'Identifier',
        'init': 'Expression'
    }

    attribute_map = {
        'type': 'type',
        'id': 'id',
        'init': 'init'
    }

    def __init__(self, type=None, id=None, init=None):  # noqa: E501,D401,D403
        """VariableAssignment - a model defined in OpenAPI."""  # noqa: E501
        Statement.__init__(self)  # noqa: E501

        self._type = None
        self._id = None
        self._init = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if id is not None:
            self.id = id
        if init is not None:
            self.init = init

    @property
    def type(self):
        """Get the type of this VariableAssignment.

        Type of AST node

        :return: The type of this VariableAssignment.
        :rtype: str
        """  # noqa: E501
        return self._type

    @type.setter
    def type(self, type):
        """Set the type of this VariableAssignment.

        Type of AST node

        :param type: The type of this VariableAssignment.
        :type: str
        """  # noqa: E501
        self._type = type

    @property
    def id(self):
        """Get the id of this VariableAssignment.

        :return: The id of this VariableAssignment.
        :rtype: Identifier
        """  # noqa: E501
        return self._id

    @id.setter
    def id(self, id):
        """Set the id of this VariableAssignment.

        :param id: The id of this VariableAssignment.
        :type: Identifier
        """  # noqa: E501
        self._id = id

    @property
    def init(self):
        """Get the init of this VariableAssignment.

        :return: The init of this VariableAssignment.
        :rtype: Expression
        """  # noqa: E501
        return self._init

    @init.setter
    def init(self, init):
        """Set the init of this VariableAssignment.

        :param init: The init of this VariableAssignment.
        :type: Expression
        """  # noqa: E501
        self._init = init

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
        if not isinstance(other, VariableAssignment):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return true if both objects are not equal."""
        return not self == other
