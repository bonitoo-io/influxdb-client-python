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
from influxdb_client.domain.notification_endpoint import NotificationEndpoint


class HTTPNotificationEndpoint(NotificationEndpoint):
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
        'url': 'str',
        'username': 'str',
        'password': 'str',
        'token': 'str',
        'method': 'str',
        'auth_method': 'str',
        'content_template': 'str',
        'headers': 'dict(str, str)'
    }

    attribute_map = {
        'url': 'url',
        'username': 'username',
        'password': 'password',
        'token': 'token',
        'method': 'method',
        'auth_method': 'authMethod',
        'content_template': 'contentTemplate',
        'headers': 'headers'
    }

    def __init__(self, url=None, username=None, password=None, token=None, method=None, auth_method=None, content_template=None, headers=None):  # noqa: E501
        """HTTPNotificationEndpoint - a model defined in OpenAPI"""  # noqa: E501
        NotificationEndpoint.__init__(self)  # noqa: E501

        self._url = None
        self._username = None
        self._password = None
        self._token = None
        self._method = None
        self._auth_method = None
        self._content_template = None
        self._headers = None
        self.discriminator = None

        self.url = url
        if username is not None:
            self.username = username
        if password is not None:
            self.password = password
        if token is not None:
            self.token = token
        self.method = method
        self.auth_method = auth_method
        if content_template is not None:
            self.content_template = content_template
        if headers is not None:
            self.headers = headers

    @property
    def url(self):
        """Gets the url of this HTTPNotificationEndpoint.  # noqa: E501


        :return: The url of this HTTPNotificationEndpoint.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this HTTPNotificationEndpoint.


        :param url: The url of this HTTPNotificationEndpoint.  # noqa: E501
        :type: str
        """
        if url is None:
            raise ValueError("Invalid value for `url`, must not be `None`")  # noqa: E501

        self._url = url

    @property
    def username(self):
        """Gets the username of this HTTPNotificationEndpoint.  # noqa: E501


        :return: The username of this HTTPNotificationEndpoint.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this HTTPNotificationEndpoint.


        :param username: The username of this HTTPNotificationEndpoint.  # noqa: E501
        :type: str
        """

        self._username = username

    @property
    def password(self):
        """Gets the password of this HTTPNotificationEndpoint.  # noqa: E501


        :return: The password of this HTTPNotificationEndpoint.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this HTTPNotificationEndpoint.


        :param password: The password of this HTTPNotificationEndpoint.  # noqa: E501
        :type: str
        """

        self._password = password

    @property
    def token(self):
        """Gets the token of this HTTPNotificationEndpoint.  # noqa: E501


        :return: The token of this HTTPNotificationEndpoint.  # noqa: E501
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token):
        """Sets the token of this HTTPNotificationEndpoint.


        :param token: The token of this HTTPNotificationEndpoint.  # noqa: E501
        :type: str
        """

        self._token = token

    @property
    def method(self):
        """Gets the method of this HTTPNotificationEndpoint.  # noqa: E501


        :return: The method of this HTTPNotificationEndpoint.  # noqa: E501
        :rtype: str
        """
        return self._method

    @method.setter
    def method(self, method):
        """Sets the method of this HTTPNotificationEndpoint.


        :param method: The method of this HTTPNotificationEndpoint.  # noqa: E501
        :type: str
        """
        if method is None:
            raise ValueError("Invalid value for `method`, must not be `None`")  # noqa: E501

        self._method = method

    @property
    def auth_method(self):
        """Gets the auth_method of this HTTPNotificationEndpoint.  # noqa: E501


        :return: The auth_method of this HTTPNotificationEndpoint.  # noqa: E501
        :rtype: str
        """
        return self._auth_method

    @auth_method.setter
    def auth_method(self, auth_method):
        """Sets the auth_method of this HTTPNotificationEndpoint.


        :param auth_method: The auth_method of this HTTPNotificationEndpoint.  # noqa: E501
        :type: str
        """
        if auth_method is None:
            raise ValueError("Invalid value for `auth_method`, must not be `None`")  # noqa: E501

        self._auth_method = auth_method

    @property
    def content_template(self):
        """Gets the content_template of this HTTPNotificationEndpoint.  # noqa: E501


        :return: The content_template of this HTTPNotificationEndpoint.  # noqa: E501
        :rtype: str
        """
        return self._content_template

    @content_template.setter
    def content_template(self, content_template):
        """Sets the content_template of this HTTPNotificationEndpoint.


        :param content_template: The content_template of this HTTPNotificationEndpoint.  # noqa: E501
        :type: str
        """

        self._content_template = content_template

    @property
    def headers(self):
        """Gets the headers of this HTTPNotificationEndpoint.  # noqa: E501

        Customized headers.  # noqa: E501

        :return: The headers of this HTTPNotificationEndpoint.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._headers

    @headers.setter
    def headers(self, headers):
        """Sets the headers of this HTTPNotificationEndpoint.

        Customized headers.  # noqa: E501

        :param headers: The headers of this HTTPNotificationEndpoint.  # noqa: E501
        :type: dict(str, str)
        """

        self._headers = headers

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
        if not isinstance(other, HTTPNotificationEndpoint):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
