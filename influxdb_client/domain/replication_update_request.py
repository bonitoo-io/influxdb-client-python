# coding: utf-8

"""
InfluxDB OSS API Service.

The InfluxDB v2 API provides a programmatic interface for all interactions with InfluxDB. Access the InfluxDB API using the `/api/v2/` endpoint.   # noqa: E501

OpenAPI spec version: 2.0.0
Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401


class ReplicationUpdateRequest(object):
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
        'remote_id': 'str',
        'remote_bucket_id': 'str',
        'max_queue_size_bytes': 'int',
        'drop_non_retryable_data': 'bool'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'remote_id': 'remoteID',
        'remote_bucket_id': 'remoteBucketID',
        'max_queue_size_bytes': 'maxQueueSizeBytes',
        'drop_non_retryable_data': 'dropNonRetryableData'
    }

    def __init__(self, name=None, description=None, remote_id=None, remote_bucket_id=None, max_queue_size_bytes=None, drop_non_retryable_data=None):  # noqa: E501,D401,D403
        """ReplicationUpdateRequest - a model defined in OpenAPI."""  # noqa: E501
        self._name = None
        self._description = None
        self._remote_id = None
        self._remote_bucket_id = None
        self._max_queue_size_bytes = None
        self._drop_non_retryable_data = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if remote_id is not None:
            self.remote_id = remote_id
        if remote_bucket_id is not None:
            self.remote_bucket_id = remote_bucket_id
        if max_queue_size_bytes is not None:
            self.max_queue_size_bytes = max_queue_size_bytes
        if drop_non_retryable_data is not None:
            self.drop_non_retryable_data = drop_non_retryable_data

    @property
    def name(self):
        """Get the name of this ReplicationUpdateRequest.

        :return: The name of this ReplicationUpdateRequest.
        :rtype: str
        """  # noqa: E501
        return self._name

    @name.setter
    def name(self, name):
        """Set the name of this ReplicationUpdateRequest.

        :param name: The name of this ReplicationUpdateRequest.
        :type: str
        """  # noqa: E501
        self._name = name

    @property
    def description(self):
        """Get the description of this ReplicationUpdateRequest.

        :return: The description of this ReplicationUpdateRequest.
        :rtype: str
        """  # noqa: E501
        return self._description

    @description.setter
    def description(self, description):
        """Set the description of this ReplicationUpdateRequest.

        :param description: The description of this ReplicationUpdateRequest.
        :type: str
        """  # noqa: E501
        self._description = description

    @property
    def remote_id(self):
        """Get the remote_id of this ReplicationUpdateRequest.

        :return: The remote_id of this ReplicationUpdateRequest.
        :rtype: str
        """  # noqa: E501
        return self._remote_id

    @remote_id.setter
    def remote_id(self, remote_id):
        """Set the remote_id of this ReplicationUpdateRequest.

        :param remote_id: The remote_id of this ReplicationUpdateRequest.
        :type: str
        """  # noqa: E501
        self._remote_id = remote_id

    @property
    def remote_bucket_id(self):
        """Get the remote_bucket_id of this ReplicationUpdateRequest.

        :return: The remote_bucket_id of this ReplicationUpdateRequest.
        :rtype: str
        """  # noqa: E501
        return self._remote_bucket_id

    @remote_bucket_id.setter
    def remote_bucket_id(self, remote_bucket_id):
        """Set the remote_bucket_id of this ReplicationUpdateRequest.

        :param remote_bucket_id: The remote_bucket_id of this ReplicationUpdateRequest.
        :type: str
        """  # noqa: E501
        self._remote_bucket_id = remote_bucket_id

    @property
    def max_queue_size_bytes(self):
        """Get the max_queue_size_bytes of this ReplicationUpdateRequest.

        :return: The max_queue_size_bytes of this ReplicationUpdateRequest.
        :rtype: int
        """  # noqa: E501
        return self._max_queue_size_bytes

    @max_queue_size_bytes.setter
    def max_queue_size_bytes(self, max_queue_size_bytes):
        """Set the max_queue_size_bytes of this ReplicationUpdateRequest.

        :param max_queue_size_bytes: The max_queue_size_bytes of this ReplicationUpdateRequest.
        :type: int
        """  # noqa: E501
        if max_queue_size_bytes is not None and max_queue_size_bytes < 33554430:  # noqa: E501
            raise ValueError("Invalid value for `max_queue_size_bytes`, must be a value greater than or equal to `33554430`")  # noqa: E501
        self._max_queue_size_bytes = max_queue_size_bytes

    @property
    def drop_non_retryable_data(self):
        """Get the drop_non_retryable_data of this ReplicationUpdateRequest.

        :return: The drop_non_retryable_data of this ReplicationUpdateRequest.
        :rtype: bool
        """  # noqa: E501
        return self._drop_non_retryable_data

    @drop_non_retryable_data.setter
    def drop_non_retryable_data(self, drop_non_retryable_data):
        """Set the drop_non_retryable_data of this ReplicationUpdateRequest.

        :param drop_non_retryable_data: The drop_non_retryable_data of this ReplicationUpdateRequest.
        :type: bool
        """  # noqa: E501
        self._drop_non_retryable_data = drop_non_retryable_data

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
        if not isinstance(other, ReplicationUpdateRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return true if both objects are not equal."""
        return not self == other
