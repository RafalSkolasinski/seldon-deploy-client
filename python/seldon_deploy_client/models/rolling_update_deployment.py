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


class RollingUpdateDeployment(object):
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
        'max_surge': 'IntOrString',
        'max_unavailable': 'IntOrString'
    }

    attribute_map = {
        'max_surge': 'maxSurge',
        'max_unavailable': 'maxUnavailable'
    }

    def __init__(self, max_surge=None, max_unavailable=None):  # noqa: E501
        """RollingUpdateDeployment - a model defined in Swagger"""  # noqa: E501

        self._max_surge = None
        self._max_unavailable = None
        self.discriminator = None

        if max_surge is not None:
            self.max_surge = max_surge
        if max_unavailable is not None:
            self.max_unavailable = max_unavailable

    @property
    def max_surge(self):
        """Gets the max_surge of this RollingUpdateDeployment.  # noqa: E501


        :return: The max_surge of this RollingUpdateDeployment.  # noqa: E501
        :rtype: IntOrString
        """
        return self._max_surge

    @max_surge.setter
    def max_surge(self, max_surge):
        """Sets the max_surge of this RollingUpdateDeployment.


        :param max_surge: The max_surge of this RollingUpdateDeployment.  # noqa: E501
        :type: IntOrString
        """

        self._max_surge = max_surge

    @property
    def max_unavailable(self):
        """Gets the max_unavailable of this RollingUpdateDeployment.  # noqa: E501


        :return: The max_unavailable of this RollingUpdateDeployment.  # noqa: E501
        :rtype: IntOrString
        """
        return self._max_unavailable

    @max_unavailable.setter
    def max_unavailable(self, max_unavailable):
        """Sets the max_unavailable of this RollingUpdateDeployment.


        :param max_unavailable: The max_unavailable of this RollingUpdateDeployment.  # noqa: E501
        :type: IntOrString
        """

        self._max_unavailable = max_unavailable

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
        if issubclass(RollingUpdateDeployment, dict):
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
        if not isinstance(other, RollingUpdateDeployment):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
