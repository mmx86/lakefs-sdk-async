# coding: utf-8

"""
    lakeFS API

    lakeFS HTTP API

    The version of the OpenAPI document: 1.0.0
    Contact: services@treeverse.io
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

import lakefs_sdk_async
from lakefs_sdk_async.models.access_key_credentials import AccessKeyCredentials  # noqa: E501
from lakefs_sdk_async.rest import ApiException

class TestAccessKeyCredentials(unittest.TestCase):
    """AccessKeyCredentials unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test AccessKeyCredentials
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AccessKeyCredentials`
        """
        model = lakefs_sdk_async.models.access_key_credentials.AccessKeyCredentials()  # noqa: E501
        if include_optional :
            return AccessKeyCredentials(
                access_key_id = 'AKIAIOSFODNN7EXAMPLE', 
                secret_access_key = 'wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY'
            )
        else :
            return AccessKeyCredentials(
                access_key_id = 'AKIAIOSFODNN7EXAMPLE',
                secret_access_key = 'wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY',
        )
        """

    def testAccessKeyCredentials(self):
        """Test AccessKeyCredentials"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
