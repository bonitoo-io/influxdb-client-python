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


class LineProtocolError(object):
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
        'code': 'str',
        'message': 'str',
        'op': 'str',
        'err': 'str',
        'line': 'int'
    }

    attribute_map = {
        'code': 'code',
        'message': 'message',
        'op': 'op',
        'err': 'err',
        'line': 'line'
    }

    def __init__(self, code=None, message=None, op=None, err=None, line=None):  # noqa: E501,D401,D403
        """LineProtocolError - a model defined in OpenAPI."""  # noqa: E501
        self._code = None
        self._message = None
        self._op = None
        self._err = None
        self._line = None
        self.discriminator = None

        self.code = code
        self.message = message
        self.op = op
        self.err = err
        if line is not None:
            self.line = line

    @property
    def code(self):
        """Get the code of this LineProtocolError.

        Code is the machine-readable error code.

        :return: The code of this LineProtocolError.
        :rtype: str
        """  # noqa: E501
        return self._code

    @code.setter
    def code(self, code):
        """Set the code of this LineProtocolError.

        Code is the machine-readable error code.

        :param code: The code of this LineProtocolError.
        :type: str
        """  # noqa: E501
        if code is None:
            raise ValueError("Invalid value for `code`, must not be `None`")  # noqa: E501
        self._code = code

    @property
    def message(self):
        """Get the message of this LineProtocolError.

        Message is a human-readable message.

        :return: The message of this LineProtocolError.
        :rtype: str
        """  # noqa: E501
        return self._message

    @message.setter
    def message(self, message):
        """Set the message of this LineProtocolError.

        Message is a human-readable message.

        :param message: The message of this LineProtocolError.
        :type: str
        """  # noqa: E501
        if message is None:
            raise ValueError("Invalid value for `message`, must not be `None`")  # noqa: E501
        self._message = message

    @property
    def op(self):
        """Get the op of this LineProtocolError.

        Op describes the logical code operation during error. Useful for debugging.

        :return: The op of this LineProtocolError.
        :rtype: str
        """  # noqa: E501
        return self._op

    @op.setter
    def op(self, op):
        """Set the op of this LineProtocolError.

        Op describes the logical code operation during error. Useful for debugging.

        :param op: The op of this LineProtocolError.
        :type: str
        """  # noqa: E501
        if op is None:
            raise ValueError("Invalid value for `op`, must not be `None`")  # noqa: E501
        self._op = op

    @property
    def err(self):
        """Get the err of this LineProtocolError.

        Err is a stack of errors that occurred during processing of the request. Useful for debugging.

        :return: The err of this LineProtocolError.
        :rtype: str
        """  # noqa: E501
        return self._err

    @err.setter
    def err(self, err):
        """Set the err of this LineProtocolError.

        Err is a stack of errors that occurred during processing of the request. Useful for debugging.

        :param err: The err of this LineProtocolError.
        :type: str
        """  # noqa: E501
        if err is None:
            raise ValueError("Invalid value for `err`, must not be `None`")  # noqa: E501
        self._err = err

    @property
    def line(self):
        """Get the line of this LineProtocolError.

        First line within sent body containing malformed data

        :return: The line of this LineProtocolError.
        :rtype: int
        """  # noqa: E501
        return self._line

    @line.setter
    def line(self, line):
        """Set the line of this LineProtocolError.

        First line within sent body containing malformed data

        :param line: The line of this LineProtocolError.
        :type: int
        """  # noqa: E501
        self._line = line

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
        if not isinstance(other, LineProtocolError):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return true if both objects are not equal."""
        return not self == other
