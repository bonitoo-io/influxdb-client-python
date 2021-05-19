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


class CheckBaseLinks(object):
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
        '_self': 'str',
        'labels': 'str',
        'members': 'str',
        'owners': 'str',
        'query': 'str'
    }

    attribute_map = {
        '_self': 'self',
        'labels': 'labels',
        'members': 'members',
        'owners': 'owners',
        'query': 'query'
    }

    def __init__(self, _self=None, labels=None, members=None, owners=None, query=None):  # noqa: E501,D401,D403
        """CheckBaseLinks - a model defined in OpenAPI."""  # noqa: E501
        self.__self = None
        self._labels = None
        self._members = None
        self._owners = None
        self._query = None
        self.discriminator = None

        if _self is not None:
            self._self = _self
        if labels is not None:
            self.labels = labels
        if members is not None:
            self.members = members
        if owners is not None:
            self.owners = owners
        if query is not None:
            self.query = query

    @property
    def _self(self):
        """Get the _self of this CheckBaseLinks.

        URI of resource.

        :return: The _self of this CheckBaseLinks.
        :rtype: str
        """  # noqa: E501
        return self.__self

    @_self.setter
    def _self(self, _self):
        """Set the _self of this CheckBaseLinks.

        URI of resource.

        :param _self: The _self of this CheckBaseLinks.
        :type: str
        """  # noqa: E501
        self.__self = _self

    @property
    def labels(self):
        """Get the labels of this CheckBaseLinks.

        URI of resource.

        :return: The labels of this CheckBaseLinks.
        :rtype: str
        """  # noqa: E501
        return self._labels

    @labels.setter
    def labels(self, labels):
        """Set the labels of this CheckBaseLinks.

        URI of resource.

        :param labels: The labels of this CheckBaseLinks.
        :type: str
        """  # noqa: E501
        self._labels = labels

    @property
    def members(self):
        """Get the members of this CheckBaseLinks.

        URI of resource.

        :return: The members of this CheckBaseLinks.
        :rtype: str
        """  # noqa: E501
        return self._members

    @members.setter
    def members(self, members):
        """Set the members of this CheckBaseLinks.

        URI of resource.

        :param members: The members of this CheckBaseLinks.
        :type: str
        """  # noqa: E501
        self._members = members

    @property
    def owners(self):
        """Get the owners of this CheckBaseLinks.

        URI of resource.

        :return: The owners of this CheckBaseLinks.
        :rtype: str
        """  # noqa: E501
        return self._owners

    @owners.setter
    def owners(self, owners):
        """Set the owners of this CheckBaseLinks.

        URI of resource.

        :param owners: The owners of this CheckBaseLinks.
        :type: str
        """  # noqa: E501
        self._owners = owners

    @property
    def query(self):
        """Get the query of this CheckBaseLinks.

        URI of resource.

        :return: The query of this CheckBaseLinks.
        :rtype: str
        """  # noqa: E501
        return self._query

    @query.setter
    def query(self, query):
        """Set the query of this CheckBaseLinks.

        URI of resource.

        :param query: The query of this CheckBaseLinks.
        :type: str
        """  # noqa: E501
        self._query = query

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
        if not isinstance(other, CheckBaseLinks):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return true if both objects are not equal."""
        return not self == other
