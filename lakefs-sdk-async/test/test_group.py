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
from lakefs_sdk_async.models.group import Group  # noqa: E501
from lakefs_sdk_async.rest import ApiException

class TestGroup(unittest.TestCase):
    """Group unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Group
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Group`
        """
        model = lakefs_sdk_async.models.group.Group()  # noqa: E501
        if include_optional :
            return Group(
                id = '', 
                name = '', 
                description = '', 
                creation_date = 56
            )
        else :
            return Group(
                id = '',
                creation_date = 56,
        )
        """

    def testGroup(self):
        """Test Group"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
