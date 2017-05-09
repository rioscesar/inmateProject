# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class NodeRemoveParameter(Model):
    """Parameters for a ComputeNodeOperations.Remove request.

    :param node_list: A list containing the ids of the compute nodes to be
     removed from the specified pool.
    :type node_list: list of str
    :param resize_timeout: The timeout for removal of compute nodes to the
     pool. The default value is 10 minutes.
    :type resize_timeout: timedelta
    :param node_deallocation_option: When compute nodes may be removed from
     the pool. Possible values include: 'requeue', 'terminate',
     'taskcompletion', 'retaineddata'
    :type node_deallocation_option: str or
     :class:`ComputeNodeDeallocationOption
     <azure.batch.models.ComputeNodeDeallocationOption>`
    """ 

    _validation = {
        'node_list': {'required': True, 'max_items': 100},
    }

    _attribute_map = {
        'node_list': {'key': 'nodeList', 'type': '[str]'},
        'resize_timeout': {'key': 'resizeTimeout', 'type': 'duration'},
        'node_deallocation_option': {'key': 'nodeDeallocationOption', 'type': 'ComputeNodeDeallocationOption'},
    }

    def __init__(self, node_list, resize_timeout=None, node_deallocation_option=None):
        self.node_list = node_list
        self.resize_timeout = resize_timeout
        self.node_deallocation_option = node_deallocation_option
