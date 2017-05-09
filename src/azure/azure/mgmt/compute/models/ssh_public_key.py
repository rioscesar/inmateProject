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


class SshPublicKey(Model):
    """Contains information about SSH certificate public key and the path on the
    Linux VM where the public key is placed.

    :param path: the full path on the created VM where SSH public key is
     stored. If the file already exists, the specified key is appended to the
     file.
    :type path: str
    :param key_data: Certificate public key used to authenticate with VM
     through SSH.The certificate must be in Pem format with or without
     headers.
    :type key_data: str
    """ 

    _attribute_map = {
        'path': {'key': 'path', 'type': 'str'},
        'key_data': {'key': 'keyData', 'type': 'str'},
    }

    def __init__(self, path=None, key_data=None):
        self.path = path
        self.key_data = key_data
