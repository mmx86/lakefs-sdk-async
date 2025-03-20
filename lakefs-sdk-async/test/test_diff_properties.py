# coding: utf-8

"""
    lakeFS API

    lakeFS HTTP API

    The version of the OpenAPI document: 0.1.0
    Contact: services@treeverse.io
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

import lakefs_sdk_async
from lakefs_sdk_async.models.diff_properties import DiffProperties  # noqa: E501
from lakefs_sdk_async.rest import ApiException

class TestDiffProperties(unittest.TestCase):
    """DiffProperties unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test DiffProperties
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DiffProperties`
        """
        model = lakefs_sdk_async.models.diff_properties.DiffProperties()  # noqa: E501
        if include_optional :
            return DiffProperties(
                name = ''
            )
        else :
            return DiffProperties(
                name = '',
        )
        """

    def testDiffProperties(self):
        """Test DiffProperties"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
