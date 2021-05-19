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


class CheckBase(object):
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
        'org_id': 'str',
        'task_id': 'str',
        'owner_id': 'str',
        'created_at': 'datetime',
        'updated_at': 'datetime',
        'query': 'DashboardQuery',
        'status': 'TaskStatusType',
        'description': 'str',
        'latest_completed': 'datetime',
        'last_run_status': 'str',
        'last_run_error': 'str',
        'labels': 'list[Label]',
        'links': 'CheckBaseLinks'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'org_id': 'orgID',
        'task_id': 'taskID',
        'owner_id': 'ownerID',
        'created_at': 'createdAt',
        'updated_at': 'updatedAt',
        'query': 'query',
        'status': 'status',
        'description': 'description',
        'latest_completed': 'latestCompleted',
        'last_run_status': 'lastRunStatus',
        'last_run_error': 'lastRunError',
        'labels': 'labels',
        'links': 'links'
    }

    def __init__(self, id=None, name=None, org_id=None, task_id=None, owner_id=None, created_at=None, updated_at=None, query=None, status=None, description=None, latest_completed=None, last_run_status=None, last_run_error=None, labels=None, links=None):  # noqa: E501,D401,D403
        """CheckBase - a model defined in OpenAPI."""  # noqa: E501
        self._id = None
        self._name = None
        self._org_id = None
        self._task_id = None
        self._owner_id = None
        self._created_at = None
        self._updated_at = None
        self._query = None
        self._status = None
        self._description = None
        self._latest_completed = None
        self._last_run_status = None
        self._last_run_error = None
        self._labels = None
        self._links = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.name = name
        self.org_id = org_id
        if task_id is not None:
            self.task_id = task_id
        if owner_id is not None:
            self.owner_id = owner_id
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        self.query = query
        if status is not None:
            self.status = status
        if description is not None:
            self.description = description
        if latest_completed is not None:
            self.latest_completed = latest_completed
        if last_run_status is not None:
            self.last_run_status = last_run_status
        if last_run_error is not None:
            self.last_run_error = last_run_error
        if labels is not None:
            self.labels = labels
        if links is not None:
            self.links = links

    @property
    def id(self):
        """Get the id of this CheckBase.

        :return: The id of this CheckBase.
        :rtype: str
        """  # noqa: E501
        return self._id

    @id.setter
    def id(self, id):
        """Set the id of this CheckBase.

        :param id: The id of this CheckBase.
        :type: str
        """  # noqa: E501
        self._id = id

    @property
    def name(self):
        """Get the name of this CheckBase.

        :return: The name of this CheckBase.
        :rtype: str
        """  # noqa: E501
        return self._name

    @name.setter
    def name(self, name):
        """Set the name of this CheckBase.

        :param name: The name of this CheckBase.
        :type: str
        """  # noqa: E501
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        self._name = name

    @property
    def org_id(self):
        """Get the org_id of this CheckBase.

        The ID of the organization that owns this check.

        :return: The org_id of this CheckBase.
        :rtype: str
        """  # noqa: E501
        return self._org_id

    @org_id.setter
    def org_id(self, org_id):
        """Set the org_id of this CheckBase.

        The ID of the organization that owns this check.

        :param org_id: The org_id of this CheckBase.
        :type: str
        """  # noqa: E501
        if org_id is None:
            raise ValueError("Invalid value for `org_id`, must not be `None`")  # noqa: E501
        self._org_id = org_id

    @property
    def task_id(self):
        """Get the task_id of this CheckBase.

        The ID of the task associated with this check.

        :return: The task_id of this CheckBase.
        :rtype: str
        """  # noqa: E501
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        """Set the task_id of this CheckBase.

        The ID of the task associated with this check.

        :param task_id: The task_id of this CheckBase.
        :type: str
        """  # noqa: E501
        self._task_id = task_id

    @property
    def owner_id(self):
        """Get the owner_id of this CheckBase.

        The ID of creator used to create this check.

        :return: The owner_id of this CheckBase.
        :rtype: str
        """  # noqa: E501
        return self._owner_id

    @owner_id.setter
    def owner_id(self, owner_id):
        """Set the owner_id of this CheckBase.

        The ID of creator used to create this check.

        :param owner_id: The owner_id of this CheckBase.
        :type: str
        """  # noqa: E501
        self._owner_id = owner_id

    @property
    def created_at(self):
        """Get the created_at of this CheckBase.

        :return: The created_at of this CheckBase.
        :rtype: datetime
        """  # noqa: E501
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Set the created_at of this CheckBase.

        :param created_at: The created_at of this CheckBase.
        :type: datetime
        """  # noqa: E501
        self._created_at = created_at

    @property
    def updated_at(self):
        """Get the updated_at of this CheckBase.

        :return: The updated_at of this CheckBase.
        :rtype: datetime
        """  # noqa: E501
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Set the updated_at of this CheckBase.

        :param updated_at: The updated_at of this CheckBase.
        :type: datetime
        """  # noqa: E501
        self._updated_at = updated_at

    @property
    def query(self):
        """Get the query of this CheckBase.

        :return: The query of this CheckBase.
        :rtype: DashboardQuery
        """  # noqa: E501
        return self._query

    @query.setter
    def query(self, query):
        """Set the query of this CheckBase.

        :param query: The query of this CheckBase.
        :type: DashboardQuery
        """  # noqa: E501
        if query is None:
            raise ValueError("Invalid value for `query`, must not be `None`")  # noqa: E501
        self._query = query

    @property
    def status(self):
        """Get the status of this CheckBase.

        :return: The status of this CheckBase.
        :rtype: TaskStatusType
        """  # noqa: E501
        return self._status

    @status.setter
    def status(self, status):
        """Set the status of this CheckBase.

        :param status: The status of this CheckBase.
        :type: TaskStatusType
        """  # noqa: E501
        self._status = status

    @property
    def description(self):
        """Get the description of this CheckBase.

        An optional description of the check.

        :return: The description of this CheckBase.
        :rtype: str
        """  # noqa: E501
        return self._description

    @description.setter
    def description(self, description):
        """Set the description of this CheckBase.

        An optional description of the check.

        :param description: The description of this CheckBase.
        :type: str
        """  # noqa: E501
        self._description = description

    @property
    def latest_completed(self):
        """Get the latest_completed of this CheckBase.

        Timestamp of latest scheduled, completed run, RFC3339.

        :return: The latest_completed of this CheckBase.
        :rtype: datetime
        """  # noqa: E501
        return self._latest_completed

    @latest_completed.setter
    def latest_completed(self, latest_completed):
        """Set the latest_completed of this CheckBase.

        Timestamp of latest scheduled, completed run, RFC3339.

        :param latest_completed: The latest_completed of this CheckBase.
        :type: datetime
        """  # noqa: E501
        self._latest_completed = latest_completed

    @property
    def last_run_status(self):
        """Get the last_run_status of this CheckBase.

        :return: The last_run_status of this CheckBase.
        :rtype: str
        """  # noqa: E501
        return self._last_run_status

    @last_run_status.setter
    def last_run_status(self, last_run_status):
        """Set the last_run_status of this CheckBase.

        :param last_run_status: The last_run_status of this CheckBase.
        :type: str
        """  # noqa: E501
        self._last_run_status = last_run_status

    @property
    def last_run_error(self):
        """Get the last_run_error of this CheckBase.

        :return: The last_run_error of this CheckBase.
        :rtype: str
        """  # noqa: E501
        return self._last_run_error

    @last_run_error.setter
    def last_run_error(self, last_run_error):
        """Set the last_run_error of this CheckBase.

        :param last_run_error: The last_run_error of this CheckBase.
        :type: str
        """  # noqa: E501
        self._last_run_error = last_run_error

    @property
    def labels(self):
        """Get the labels of this CheckBase.

        :return: The labels of this CheckBase.
        :rtype: list[Label]
        """  # noqa: E501
        return self._labels

    @labels.setter
    def labels(self, labels):
        """Set the labels of this CheckBase.

        :param labels: The labels of this CheckBase.
        :type: list[Label]
        """  # noqa: E501
        self._labels = labels

    @property
    def links(self):
        """Get the links of this CheckBase.

        :return: The links of this CheckBase.
        :rtype: CheckBaseLinks
        """  # noqa: E501
        return self._links

    @links.setter
    def links(self, links):
        """Set the links of this CheckBase.

        :param links: The links of this CheckBase.
        :type: CheckBaseLinks
        """  # noqa: E501
        self._links = links

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
        if not isinstance(other, CheckBase):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return true if both objects are not equal."""
        return not self == other
