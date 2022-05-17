# coding: utf-8

"""
InfluxDB OSS API Service.

The InfluxDB v2 API provides a programmatic interface for all interactions with InfluxDB. Access the InfluxDB API using the `/api/v2/` endpoint.   # noqa: E501

OpenAPI spec version: 2.0.0
Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401


class TemplateSummaryDiffDashboardsNewOld(object):
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
        'description': 'str',
        'charts': 'list[TemplateChart]'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'charts': 'charts'
    }

    def __init__(self, name=None, description=None, charts=None):  # noqa: E501,D401,D403
        """TemplateSummaryDiffDashboardsNewOld - a model defined in OpenAPI."""  # noqa: E501
        self._name = None
        self._description = None
        self._charts = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if charts is not None:
            self.charts = charts

    @property
    def name(self):
        """Get the name of this TemplateSummaryDiffDashboardsNewOld.

        :return: The name of this TemplateSummaryDiffDashboardsNewOld.
        :rtype: str
        """  # noqa: E501
        return self._name

    @name.setter
    def name(self, name):
        """Set the name of this TemplateSummaryDiffDashboardsNewOld.

        :param name: The name of this TemplateSummaryDiffDashboardsNewOld.
        :type: str
        """  # noqa: E501
        self._name = name

    @property
    def description(self):
        """Get the description of this TemplateSummaryDiffDashboardsNewOld.

        :return: The description of this TemplateSummaryDiffDashboardsNewOld.
        :rtype: str
        """  # noqa: E501
        return self._description

    @description.setter
    def description(self, description):
        """Set the description of this TemplateSummaryDiffDashboardsNewOld.

        :param description: The description of this TemplateSummaryDiffDashboardsNewOld.
        :type: str
        """  # noqa: E501
        self._description = description

    @property
    def charts(self):
        """Get the charts of this TemplateSummaryDiffDashboardsNewOld.

        :return: The charts of this TemplateSummaryDiffDashboardsNewOld.
        :rtype: list[TemplateChart]
        """  # noqa: E501
        return self._charts

    @charts.setter
    def charts(self, charts):
        """Set the charts of this TemplateSummaryDiffDashboardsNewOld.

        :param charts: The charts of this TemplateSummaryDiffDashboardsNewOld.
        :type: list[TemplateChart]
        """  # noqa: E501
        self._charts = charts

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
        if not isinstance(other, TemplateSummaryDiffDashboardsNewOld):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return true if both objects are not equal."""
        return not self == other
