# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft and contributors.  All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class DomainControlCenterSsoRequest(Model):
    """Single sign on request information for domain management.

    :param url: Url where the single sign on request is to be made
    :type url: str
    :param post_parameter_key: Post parameter key
    :type post_parameter_key: str
    :param post_parameter_value: Post parameter value. Client should use
     'application/x-www-form-urlencoded' encoding for this value.
    :type post_parameter_value: str
    """ 

    _attribute_map = {
        'url': {'key': 'url', 'type': 'str'},
        'post_parameter_key': {'key': 'postParameterKey', 'type': 'str'},
        'post_parameter_value': {'key': 'postParameterValue', 'type': 'str'},
    }

    def __init__(self, url=None, post_parameter_key=None, post_parameter_value=None):
        self.url = url
        self.post_parameter_key = post_parameter_key
        self.post_parameter_value = post_parameter_value
