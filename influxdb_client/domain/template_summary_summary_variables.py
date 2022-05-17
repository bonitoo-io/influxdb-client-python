# coding: utf-8

"""
InfluxDB OSS API Service.

The InfluxDB v2 API provides a programmatic interface for all interactions with InfluxDB. Access the InfluxDB API using the `/api/v2/` endpoint.   # noqa: E501

OpenAPI spec version: 2.0.0
Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401


class TemplateSummarySummaryVariables(object):
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
        'kind': 'TemplateKind',
        'template_meta_name': 'str',
        'id': 'str',
        'org_id': 'str',
        'name': 'str',
        'description': 'str',
        'arguments': 'VariableProperties',
        'label_associations': 'list[TemplateSummaryLabel]',
        'env_references': 'list[object]'
    }

    attribute_map = {
        'kind': 'kind',
        'template_meta_name': 'templateMetaName',
        'id': 'id',
        'org_id': 'orgID',
        'name': 'name',
        'description': 'description',
        'arguments': 'arguments',
        'label_associations': 'labelAssociations',
        'env_references': 'envReferences'
    }

    def __init__(self, kind=None, template_meta_name=None, id=None, org_id=None, name=None, description=None, arguments=None, label_associations=None, env_references=None):  # noqa: E501,D401,D403
        """TemplateSummarySummaryVariables - a model defined in OpenAPI."""  # noqa: E501
        self._kind = None
        self._template_meta_name = None
        self._id = None
        self._org_id = None
        self._name = None
        self._description = None
        self._arguments = None
        self._label_associations = None
        self._env_references = None
        self.discriminator = None

        if kind is not None:
            self.kind = kind
        if template_meta_name is not None:
            self.template_meta_name = template_meta_name
        if id is not None:
            self.id = id
        if org_id is not None:
            self.org_id = org_id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if arguments is not None:
            self.arguments = arguments
        if label_associations is not None:
            self.label_associations = label_associations
        if env_references is not None:
            self.env_references = env_references

    @property
    def kind(self):
        """Get the kind of this TemplateSummarySummaryVariables.

        :return: The kind of this TemplateSummarySummaryVariables.
        :rtype: TemplateKind
        """  # noqa: E501
        return self._kind

    @kind.setter
    def kind(self, kind):
        """Set the kind of this TemplateSummarySummaryVariables.

        :param kind: The kind of this TemplateSummarySummaryVariables.
        :type: TemplateKind
        """  # noqa: E501
        self._kind = kind

    @property
    def template_meta_name(self):
        """Get the template_meta_name of this TemplateSummarySummaryVariables.

        :return: The template_meta_name of this TemplateSummarySummaryVariables.
        :rtype: str
        """  # noqa: E501
        return self._template_meta_name

    @template_meta_name.setter
    def template_meta_name(self, template_meta_name):
        """Set the template_meta_name of this TemplateSummarySummaryVariables.

        :param template_meta_name: The template_meta_name of this TemplateSummarySummaryVariables.
        :type: str
        """  # noqa: E501
        self._template_meta_name = template_meta_name

    @property
    def id(self):
        """Get the id of this TemplateSummarySummaryVariables.

        :return: The id of this TemplateSummarySummaryVariables.
        :rtype: str
        """  # noqa: E501
        return self._id

    @id.setter
    def id(self, id):
        """Set the id of this TemplateSummarySummaryVariables.

        :param id: The id of this TemplateSummarySummaryVariables.
        :type: str
        """  # noqa: E501
        self._id = id

    @property
    def org_id(self):
        """Get the org_id of this TemplateSummarySummaryVariables.

        :return: The org_id of this TemplateSummarySummaryVariables.
        :rtype: str
        """  # noqa: E501
        return self._org_id

    @org_id.setter
    def org_id(self, org_id):
        """Set the org_id of this TemplateSummarySummaryVariables.

        :param org_id: The org_id of this TemplateSummarySummaryVariables.
        :type: str
        """  # noqa: E501
        self._org_id = org_id

    @property
    def name(self):
        """Get the name of this TemplateSummarySummaryVariables.

        :return: The name of this TemplateSummarySummaryVariables.
        :rtype: str
        """  # noqa: E501
        return self._name

    @name.setter
    def name(self, name):
        """Set the name of this TemplateSummarySummaryVariables.

        :param name: The name of this TemplateSummarySummaryVariables.
        :type: str
        """  # noqa: E501
        self._name = name

    @property
    def description(self):
        """Get the description of this TemplateSummarySummaryVariables.

        :return: The description of this TemplateSummarySummaryVariables.
        :rtype: str
        """  # noqa: E501
        return self._description

    @description.setter
    def description(self, description):
        """Set the description of this TemplateSummarySummaryVariables.

        :param description: The description of this TemplateSummarySummaryVariables.
        :type: str
        """  # noqa: E501
        self._description = description

    @property
    def arguments(self):
        """Get the arguments of this TemplateSummarySummaryVariables.

        :return: The arguments of this TemplateSummarySummaryVariables.
        :rtype: VariableProperties
        """  # noqa: E501
        return self._arguments

    @arguments.setter
    def arguments(self, arguments):
        """Set the arguments of this TemplateSummarySummaryVariables.

        :param arguments: The arguments of this TemplateSummarySummaryVariables.
        :type: VariableProperties
        """  # noqa: E501
        self._arguments = arguments

    @property
    def label_associations(self):
        """Get the label_associations of this TemplateSummarySummaryVariables.

        :return: The label_associations of this TemplateSummarySummaryVariables.
        :rtype: list[TemplateSummaryLabel]
        """  # noqa: E501
        return self._label_associations

    @label_associations.setter
    def label_associations(self, label_associations):
        """Set the label_associations of this TemplateSummarySummaryVariables.

        :param label_associations: The label_associations of this TemplateSummarySummaryVariables.
        :type: list[TemplateSummaryLabel]
        """  # noqa: E501
        self._label_associations = label_associations

    @property
    def env_references(self):
        """Get the env_references of this TemplateSummarySummaryVariables.

        :return: The env_references of this TemplateSummarySummaryVariables.
        :rtype: list[object]
        """  # noqa: E501
        return self._env_references

    @env_references.setter
    def env_references(self, env_references):
        """Set the env_references of this TemplateSummarySummaryVariables.

        :param env_references: The env_references of this TemplateSummarySummaryVariables.
        :type: list[object]
        """  # noqa: E501
        self._env_references = env_references

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
        if not isinstance(other, TemplateSummarySummaryVariables):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return true if both objects are not equal."""
        return not self == other
