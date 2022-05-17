# coding: utf-8

"""
InfluxDB OSS API Service.

The InfluxDB v2 API provides a programmatic interface for all interactions with InfluxDB. Access the InfluxDB API using the `/api/v2/` endpoint.   # noqa: E501

OpenAPI spec version: 2.0.0
Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401


class TaskCreateRequest(object):
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
        'org_id': 'str',
        'org': 'str',
        'status': 'TaskStatusType',
        'flux': 'str',
        'description': 'str'
    }

    attribute_map = {
        'org_id': 'orgID',
        'org': 'org',
        'status': 'status',
        'flux': 'flux',
        'description': 'description'
    }

    def __init__(self, org_id=None, org=None, status=None, flux=None, description=None):  # noqa: E501,D401,D403
        """TaskCreateRequest - a model defined in OpenAPI."""  # noqa: E501
        self._org_id = None
        self._org = None
        self._status = None
        self._flux = None
        self._description = None
        self.discriminator = None

        if org_id is not None:
            self.org_id = org_id
        if org is not None:
            self.org = org
        if status is not None:
            self.status = status
        self.flux = flux
        if description is not None:
            self.description = description

    @property
    def org_id(self):
        """Get the org_id of this TaskCreateRequest.

        The ID of the organization that owns this Task.

        :return: The org_id of this TaskCreateRequest.
        :rtype: str
        """  # noqa: E501
        return self._org_id

    @org_id.setter
    def org_id(self, org_id):
        """Set the org_id of this TaskCreateRequest.

        The ID of the organization that owns this Task.

        :param org_id: The org_id of this TaskCreateRequest.
        :type: str
        """  # noqa: E501
        self._org_id = org_id

    @property
    def org(self):
        """Get the org of this TaskCreateRequest.

        The name of the organization that owns this Task.

        :return: The org of this TaskCreateRequest.
        :rtype: str
        """  # noqa: E501
        return self._org

    @org.setter
    def org(self, org):
        """Set the org of this TaskCreateRequest.

        The name of the organization that owns this Task.

        :param org: The org of this TaskCreateRequest.
        :type: str
        """  # noqa: E501
        self._org = org

    @property
    def status(self):
        """Get the status of this TaskCreateRequest.

        :return: The status of this TaskCreateRequest.
        :rtype: TaskStatusType
        """  # noqa: E501
        return self._status

    @status.setter
    def status(self, status):
        """Set the status of this TaskCreateRequest.

        :param status: The status of this TaskCreateRequest.
        :type: TaskStatusType
        """  # noqa: E501
        self._status = status

    @property
    def flux(self):
        """Get the flux of this TaskCreateRequest.

        The Flux script to run for this task.

        :return: The flux of this TaskCreateRequest.
        :rtype: str
        """  # noqa: E501
        return self._flux

    @flux.setter
    def flux(self, flux):
        """Set the flux of this TaskCreateRequest.

        The Flux script to run for this task.

        :param flux: The flux of this TaskCreateRequest.
        :type: str
        """  # noqa: E501
        if flux is None:
            raise ValueError("Invalid value for `flux`, must not be `None`")  # noqa: E501
        self._flux = flux

    @property
    def description(self):
        """Get the description of this TaskCreateRequest.

        An optional description of the task.

        :return: The description of this TaskCreateRequest.
        :rtype: str
        """  # noqa: E501
        return self._description

    @description.setter
    def description(self, description):
        """Set the description of this TaskCreateRequest.

        An optional description of the task.

        :param description: The description of this TaskCreateRequest.
        :type: str
        """  # noqa: E501
        self._description = description

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
        if not isinstance(other, TaskCreateRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return true if both objects are not equal."""
        return not self == other
