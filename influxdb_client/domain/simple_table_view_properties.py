# coding: utf-8

"""
InfluxDB OSS API Service.

The InfluxDB v2 API provides a programmatic interface for all interactions with InfluxDB. Access the InfluxDB API using the `/api/v2/` endpoint.   # noqa: E501

OpenAPI spec version: 2.0.0
Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

from influxdb_client.domain.view_properties import ViewProperties


class SimpleTableViewProperties(ViewProperties):
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
        'show_all': 'bool',
        'queries': 'list[DashboardQuery]',
        'shape': 'str',
        'note': 'str',
        'show_note_when_empty': 'bool'
    }

    attribute_map = {
        'type': 'type',
        'show_all': 'showAll',
        'queries': 'queries',
        'shape': 'shape',
        'note': 'note',
        'show_note_when_empty': 'showNoteWhenEmpty'
    }

    def __init__(self, type=None, show_all=None, queries=None, shape=None, note=None, show_note_when_empty=None):  # noqa: E501,D401,D403
        """SimpleTableViewProperties - a model defined in OpenAPI."""  # noqa: E501
        ViewProperties.__init__(self)  # noqa: E501

        self._type = None
        self._show_all = None
        self._queries = None
        self._shape = None
        self._note = None
        self._show_note_when_empty = None
        self.discriminator = None

        self.type = type
        self.show_all = show_all
        self.queries = queries
        self.shape = shape
        self.note = note
        self.show_note_when_empty = show_note_when_empty

    @property
    def type(self):
        """Get the type of this SimpleTableViewProperties.

        :return: The type of this SimpleTableViewProperties.
        :rtype: str
        """  # noqa: E501
        return self._type

    @type.setter
    def type(self, type):
        """Set the type of this SimpleTableViewProperties.

        :param type: The type of this SimpleTableViewProperties.
        :type: str
        """  # noqa: E501
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        self._type = type

    @property
    def show_all(self):
        """Get the show_all of this SimpleTableViewProperties.

        :return: The show_all of this SimpleTableViewProperties.
        :rtype: bool
        """  # noqa: E501
        return self._show_all

    @show_all.setter
    def show_all(self, show_all):
        """Set the show_all of this SimpleTableViewProperties.

        :param show_all: The show_all of this SimpleTableViewProperties.
        :type: bool
        """  # noqa: E501
        if show_all is None:
            raise ValueError("Invalid value for `show_all`, must not be `None`")  # noqa: E501
        self._show_all = show_all

    @property
    def queries(self):
        """Get the queries of this SimpleTableViewProperties.

        :return: The queries of this SimpleTableViewProperties.
        :rtype: list[DashboardQuery]
        """  # noqa: E501
        return self._queries

    @queries.setter
    def queries(self, queries):
        """Set the queries of this SimpleTableViewProperties.

        :param queries: The queries of this SimpleTableViewProperties.
        :type: list[DashboardQuery]
        """  # noqa: E501
        if queries is None:
            raise ValueError("Invalid value for `queries`, must not be `None`")  # noqa: E501
        self._queries = queries

    @property
    def shape(self):
        """Get the shape of this SimpleTableViewProperties.

        :return: The shape of this SimpleTableViewProperties.
        :rtype: str
        """  # noqa: E501
        return self._shape

    @shape.setter
    def shape(self, shape):
        """Set the shape of this SimpleTableViewProperties.

        :param shape: The shape of this SimpleTableViewProperties.
        :type: str
        """  # noqa: E501
        if shape is None:
            raise ValueError("Invalid value for `shape`, must not be `None`")  # noqa: E501
        self._shape = shape

    @property
    def note(self):
        """Get the note of this SimpleTableViewProperties.

        :return: The note of this SimpleTableViewProperties.
        :rtype: str
        """  # noqa: E501
        return self._note

    @note.setter
    def note(self, note):
        """Set the note of this SimpleTableViewProperties.

        :param note: The note of this SimpleTableViewProperties.
        :type: str
        """  # noqa: E501
        if note is None:
            raise ValueError("Invalid value for `note`, must not be `None`")  # noqa: E501
        self._note = note

    @property
    def show_note_when_empty(self):
        """Get the show_note_when_empty of this SimpleTableViewProperties.

        If true, will display note when empty

        :return: The show_note_when_empty of this SimpleTableViewProperties.
        :rtype: bool
        """  # noqa: E501
        return self._show_note_when_empty

    @show_note_when_empty.setter
    def show_note_when_empty(self, show_note_when_empty):
        """Set the show_note_when_empty of this SimpleTableViewProperties.

        If true, will display note when empty

        :param show_note_when_empty: The show_note_when_empty of this SimpleTableViewProperties.
        :type: bool
        """  # noqa: E501
        if show_note_when_empty is None:
            raise ValueError("Invalid value for `show_note_when_empty`, must not be `None`")  # noqa: E501
        self._show_note_when_empty = show_note_when_empty

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
        if not isinstance(other, SimpleTableViewProperties):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return true if both objects are not equal."""
        return not self == other
