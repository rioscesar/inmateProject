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


class TenantIdDescription(Model):
    """Tenant Id information.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: The fully qualified Id. For example,
     /tenants/00000000-0000-0000-0000-000000000000.
    :vartype id: str
    :ivar tenant_id: The tenantId. For example,
     00000000-0000-0000-0000-000000000000.
    :vartype tenant_id: str
    """ 

    _validation = {
        'id': {'readonly': True},
        'tenant_id': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'tenant_id': {'key': 'tenantId', 'type': 'str'},
    }

    def __init__(self):
        self.id = None
        self.tenant_id = None
