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

from lakefs_sdk_async.models.diff_list import DiffList  # noqa: E501

class TestDiffList(unittest.TestCase):
    """DiffList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DiffList:
        """Test DiffList
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DiffList`
        """
        model = DiffList()  # noqa: E501
        if include_optional:
            return DiffList(
                pagination = lakefs_sdk_async.models.pagination.Pagination(
                    has_more = True, 
                    next_offset = '', 
                    results = 0, 
                    max_per_page = 0, ),
                results = [
                    lakefs_sdk_async.models.diff.Diff(
                        type = 'added', 
                        path = '', 
                        path_type = 'common_prefix', 
                        size_bytes = 56, )
                    ]
            )
        else:
            return DiffList(
                pagination = lakefs_sdk_async.models.pagination.Pagination(
                    has_more = True, 
                    next_offset = '', 
                    results = 0, 
                    max_per_page = 0, ),
                results = [
                    lakefs_sdk_async.models.diff.Diff(
                        type = 'added', 
                        path = '', 
                        path_type = 'common_prefix', 
                        size_bytes = 56, )
                    ],
        )
        """

    def testDiffList(self):
        """Test DiffList"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
