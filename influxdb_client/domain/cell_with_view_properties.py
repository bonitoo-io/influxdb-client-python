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
from influxdb_client.domain.cell import Cell


class CellWithViewProperties(Cell):
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
        'name': 'str',
        'properties': 'ViewProperties',
        'id': 'str',
        'links': 'CellLinks',
        'x': 'int',
        'y': 'int',
        'w': 'int',
        'h': 'int',
        'view_id': 'str'
    }

    attribute_map = {
        'name': 'name',
        'properties': 'properties',
        'id': 'id',
        'links': 'links',
        'x': 'x',
        'y': 'y',
        'w': 'w',
        'h': 'h',
        'view_id': 'viewID'
    }

    def __init__(self, name=None, properties=None, id=None, links=None, x=None, y=None, w=None, h=None, view_id=None):  # noqa: E501,D401,D403
        """CellWithViewProperties - a model defined in OpenAPI."""  # noqa: E501
        Cell.__init__(self, id=id, links=links, x=x, y=y, w=w, h=h, view_id=view_id)  # noqa: E501

        self._name = None
        self._properties = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if properties is not None:
            self.properties = properties

    @property
    def name(self):
        """Get the name of this CellWithViewProperties.

        :return: The name of this CellWithViewProperties.
        :rtype: str
        """  # noqa: E501
        return self._name

    @name.setter
    def name(self, name):
        """Set the name of this CellWithViewProperties.

        :param name: The name of this CellWithViewProperties.
        :type: str
        """  # noqa: E501
        self._name = name

    @property
    def properties(self):
        """Get the properties of this CellWithViewProperties.

        :return: The properties of this CellWithViewProperties.
        :rtype: ViewProperties
        """  # noqa: E501
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Set the properties of this CellWithViewProperties.

        :param properties: The properties of this CellWithViewProperties.
        :type: ViewProperties
        """  # noqa: E501
        self._properties = properties

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
        if not isinstance(other, CellWithViewProperties):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return true if both objects are not equal."""
        return not self == other
