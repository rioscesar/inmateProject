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


class WorkflowTriggerHistoryFilter(Model):
    """WorkflowTriggerHistoryFilter.

    :param status: The status of workflow trigger history. Possible values
     include: 'NotSpecified', 'Paused', 'Running', 'Waiting', 'Succeeded',
     'Skipped', 'Suspended', 'Cancelled', 'Failed', 'Faulted', 'TimedOut',
     'Aborted', 'Ignored'
    :type status: str or :class:`WorkflowStatus
     <azure.mgmt.logic.models.WorkflowStatus>`
    """ 

    _attribute_map = {
        'status': {'key': 'status', 'type': 'WorkflowStatus'},
    }

    def __init__(self, status=None):
        self.status = status
