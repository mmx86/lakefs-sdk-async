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
from lakefs_sdk_async.models.otf_diff_entry import OtfDiffEntry  # noqa: E501
from lakefs_sdk_async.rest import ApiException

class TestOtfDiffEntry(unittest.TestCase):
    """OtfDiffEntry unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test OtfDiffEntry
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `OtfDiffEntry`
        """
        model = lakefs_sdk_async.models.otf_diff_entry.OtfDiffEntry()  # noqa: E501
        if include_optional :
            return OtfDiffEntry(
                id = '', 
                timestamp = 56, 
                operation = '', 
                operation_content = None, 
                operation_type = 'create'
            )
        else :
            return OtfDiffEntry(
                id = '',
                timestamp = 56,
                operation = '',
                operation_content = None,
                operation_type = 'create',
        )
        """

    def testOtfDiffEntry(self):
        """Test OtfDiffEntry"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
