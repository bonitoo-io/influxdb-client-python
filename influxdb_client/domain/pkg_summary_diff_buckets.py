# coding: utf-8

"""
    Influx API Service

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    OpenAPI spec version: 0.1.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class PkgSummaryDiffBuckets(object):
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
        'id': 'str',
        'name': 'str',
        'old_description': 'str',
        'new_description': 'str',
        'old_rp': 'str',
        'new_rp': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'old_description': 'oldDescription',
        'new_description': 'newDescription',
        'old_rp': 'oldRP',
        'new_rp': 'newRP'
    }

    def __init__(self, id=None, name=None, old_description=None, new_description=None, old_rp=None, new_rp=None):  # noqa: E501
        """PkgSummaryDiffBuckets - a model defined in OpenAPI"""  # noqa: E501

        self._id = None
        self._name = None
        self._old_description = None
        self._new_description = None
        self._old_rp = None
        self._new_rp = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if old_description is not None:
            self.old_description = old_description
        if new_description is not None:
            self.new_description = new_description
        if old_rp is not None:
            self.old_rp = old_rp
        if new_rp is not None:
            self.new_rp = new_rp

    @property
    def id(self):
        """Gets the id of this PkgSummaryDiffBuckets.  # noqa: E501


        :return: The id of this PkgSummaryDiffBuckets.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PkgSummaryDiffBuckets.


        :param id: The id of this PkgSummaryDiffBuckets.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this PkgSummaryDiffBuckets.  # noqa: E501


        :return: The name of this PkgSummaryDiffBuckets.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PkgSummaryDiffBuckets.


        :param name: The name of this PkgSummaryDiffBuckets.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def old_description(self):
        """Gets the old_description of this PkgSummaryDiffBuckets.  # noqa: E501


        :return: The old_description of this PkgSummaryDiffBuckets.  # noqa: E501
        :rtype: str
        """
        return self._old_description

    @old_description.setter
    def old_description(self, old_description):
        """Sets the old_description of this PkgSummaryDiffBuckets.


        :param old_description: The old_description of this PkgSummaryDiffBuckets.  # noqa: E501
        :type: str
        """

        self._old_description = old_description

    @property
    def new_description(self):
        """Gets the new_description of this PkgSummaryDiffBuckets.  # noqa: E501


        :return: The new_description of this PkgSummaryDiffBuckets.  # noqa: E501
        :rtype: str
        """
        return self._new_description

    @new_description.setter
    def new_description(self, new_description):
        """Sets the new_description of this PkgSummaryDiffBuckets.


        :param new_description: The new_description of this PkgSummaryDiffBuckets.  # noqa: E501
        :type: str
        """

        self._new_description = new_description

    @property
    def old_rp(self):
        """Gets the old_rp of this PkgSummaryDiffBuckets.  # noqa: E501


        :return: The old_rp of this PkgSummaryDiffBuckets.  # noqa: E501
        :rtype: str
        """
        return self._old_rp

    @old_rp.setter
    def old_rp(self, old_rp):
        """Sets the old_rp of this PkgSummaryDiffBuckets.


        :param old_rp: The old_rp of this PkgSummaryDiffBuckets.  # noqa: E501
        :type: str
        """

        self._old_rp = old_rp

    @property
    def new_rp(self):
        """Gets the new_rp of this PkgSummaryDiffBuckets.  # noqa: E501


        :return: The new_rp of this PkgSummaryDiffBuckets.  # noqa: E501
        :rtype: str
        """
        return self._new_rp

    @new_rp.setter
    def new_rp(self, new_rp):
        """Sets the new_rp of this PkgSummaryDiffBuckets.


        :param new_rp: The new_rp of this PkgSummaryDiffBuckets.  # noqa: E501
        :type: str
        """

        self._new_rp = new_rp

    def to_dict(self):
        """Returns the model properties as a dict"""
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
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, PkgSummaryDiffBuckets):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
