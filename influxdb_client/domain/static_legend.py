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


class StaticLegend(object):
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
        'colorize_rows': 'bool',
        'height_ratio': 'float',
        'hide': 'bool',
        'opacity': 'float',
        'orientation_threshold': 'int',
        'value_axis': 'str',
        'width_ratio': 'float'
    }

    attribute_map = {
        'colorize_rows': 'colorizeRows',
        'height_ratio': 'heightRatio',
        'hide': 'hide',
        'opacity': 'opacity',
        'orientation_threshold': 'orientationThreshold',
        'value_axis': 'valueAxis',
        'width_ratio': 'widthRatio'
    }

    def __init__(self, colorize_rows=None, height_ratio=None, hide=None, opacity=None, orientation_threshold=None, value_axis=None, width_ratio=None):  # noqa: E501,D401,D403
        """StaticLegend - a model defined in OpenAPI."""  # noqa: E501
        self._colorize_rows = None
        self._height_ratio = None
        self._hide = None
        self._opacity = None
        self._orientation_threshold = None
        self._value_axis = None
        self._width_ratio = None
        self.discriminator = None

        if colorize_rows is not None:
            self.colorize_rows = colorize_rows
        if height_ratio is not None:
            self.height_ratio = height_ratio
        if hide is not None:
            self.hide = hide
        if opacity is not None:
            self.opacity = opacity
        if orientation_threshold is not None:
            self.orientation_threshold = orientation_threshold
        if value_axis is not None:
            self.value_axis = value_axis
        if width_ratio is not None:
            self.width_ratio = width_ratio

    @property
    def colorize_rows(self):
        """Get the colorize_rows of this StaticLegend.

        :return: The colorize_rows of this StaticLegend.
        :rtype: bool
        """  # noqa: E501
        return self._colorize_rows

    @colorize_rows.setter
    def colorize_rows(self, colorize_rows):
        """Set the colorize_rows of this StaticLegend.

        :param colorize_rows: The colorize_rows of this StaticLegend.
        :type: bool
        """  # noqa: E501
        self._colorize_rows = colorize_rows

    @property
    def height_ratio(self):
        """Get the height_ratio of this StaticLegend.

        :return: The height_ratio of this StaticLegend.
        :rtype: float
        """  # noqa: E501
        return self._height_ratio

    @height_ratio.setter
    def height_ratio(self, height_ratio):
        """Set the height_ratio of this StaticLegend.

        :param height_ratio: The height_ratio of this StaticLegend.
        :type: float
        """  # noqa: E501
        self._height_ratio = height_ratio

    @property
    def hide(self):
        """Get the hide of this StaticLegend.

        :return: The hide of this StaticLegend.
        :rtype: bool
        """  # noqa: E501
        return self._hide

    @hide.setter
    def hide(self, hide):
        """Set the hide of this StaticLegend.

        :param hide: The hide of this StaticLegend.
        :type: bool
        """  # noqa: E501
        self._hide = hide

    @property
    def opacity(self):
        """Get the opacity of this StaticLegend.

        :return: The opacity of this StaticLegend.
        :rtype: float
        """  # noqa: E501
        return self._opacity

    @opacity.setter
    def opacity(self, opacity):
        """Set the opacity of this StaticLegend.

        :param opacity: The opacity of this StaticLegend.
        :type: float
        """  # noqa: E501
        self._opacity = opacity

    @property
    def orientation_threshold(self):
        """Get the orientation_threshold of this StaticLegend.

        :return: The orientation_threshold of this StaticLegend.
        :rtype: int
        """  # noqa: E501
        return self._orientation_threshold

    @orientation_threshold.setter
    def orientation_threshold(self, orientation_threshold):
        """Set the orientation_threshold of this StaticLegend.

        :param orientation_threshold: The orientation_threshold of this StaticLegend.
        :type: int
        """  # noqa: E501
        self._orientation_threshold = orientation_threshold

    @property
    def value_axis(self):
        """Get the value_axis of this StaticLegend.

        :return: The value_axis of this StaticLegend.
        :rtype: str
        """  # noqa: E501
        return self._value_axis

    @value_axis.setter
    def value_axis(self, value_axis):
        """Set the value_axis of this StaticLegend.

        :param value_axis: The value_axis of this StaticLegend.
        :type: str
        """  # noqa: E501
        self._value_axis = value_axis

    @property
    def width_ratio(self):
        """Get the width_ratio of this StaticLegend.

        :return: The width_ratio of this StaticLegend.
        :rtype: float
        """  # noqa: E501
        return self._width_ratio

    @width_ratio.setter
    def width_ratio(self, width_ratio):
        """Set the width_ratio of this StaticLegend.

        :param width_ratio: The width_ratio of this StaticLegend.
        :type: float
        """  # noqa: E501
        self._width_ratio = width_ratio

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
        if not isinstance(other, StaticLegend):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return true if both objects are not equal."""
        return not self == other
