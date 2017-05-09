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


class IntegrationAccountSchemaFilter(Model):
    """IntegrationAccountSchemaFilter.

    :param schema_type: The schema type of integration account schema.
     Possible values include: 'NotSpecified', 'Xml'
    :type schema_type: str or :class:`SchemaType
     <azure.mgmt.logic.models.SchemaType>`
    """ 

    _attribute_map = {
        'schema_type': {'key': 'schemaType', 'type': 'SchemaType'},
    }

    def __init__(self, schema_type=None):
        self.schema_type = schema_type
