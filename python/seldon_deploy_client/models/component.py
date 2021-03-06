# coding: utf-8

"""
    Seldon-Deploy API.

    Documentation of Seldon-Deploy API.  # noqa: E501

    OpenAPI spec version: v1alpha1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class Component(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'component': 'str',
        'deployments': 'DeploymentList',
        'pods': 'PodList',
        'services': 'ServiceList'
    }

    attribute_map = {
        'component': 'component',
        'deployments': 'deployments',
        'pods': 'pods',
        'services': 'services'
    }

    def __init__(self, component=None, deployments=None, pods=None, services=None):  # noqa: E501
        """Component - a model defined in Swagger"""  # noqa: E501

        self._component = None
        self._deployments = None
        self._pods = None
        self._services = None
        self.discriminator = None

        if component is not None:
            self.component = component
        if deployments is not None:
            self.deployments = deployments
        if pods is not None:
            self.pods = pods
        if services is not None:
            self.services = services

    @property
    def component(self):
        """Gets the component of this Component.  # noqa: E501


        :return: The component of this Component.  # noqa: E501
        :rtype: str
        """
        return self._component

    @component.setter
    def component(self, component):
        """Sets the component of this Component.


        :param component: The component of this Component.  # noqa: E501
        :type: str
        """

        self._component = component

    @property
    def deployments(self):
        """Gets the deployments of this Component.  # noqa: E501


        :return: The deployments of this Component.  # noqa: E501
        :rtype: DeploymentList
        """
        return self._deployments

    @deployments.setter
    def deployments(self, deployments):
        """Sets the deployments of this Component.


        :param deployments: The deployments of this Component.  # noqa: E501
        :type: DeploymentList
        """

        self._deployments = deployments

    @property
    def pods(self):
        """Gets the pods of this Component.  # noqa: E501


        :return: The pods of this Component.  # noqa: E501
        :rtype: PodList
        """
        return self._pods

    @pods.setter
    def pods(self, pods):
        """Sets the pods of this Component.


        :param pods: The pods of this Component.  # noqa: E501
        :type: PodList
        """

        self._pods = pods

    @property
    def services(self):
        """Gets the services of this Component.  # noqa: E501


        :return: The services of this Component.  # noqa: E501
        :rtype: ServiceList
        """
        return self._services

    @services.setter
    def services(self, services):
        """Sets the services of this Component.


        :param services: The services of this Component.  # noqa: E501
        :type: ServiceList
        """

        self._services = services

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(Component, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Component):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
