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

from lakefs_sdk_async.models.policy_list import PolicyList  # noqa: E501

class TestPolicyList(unittest.TestCase):
    """PolicyList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PolicyList:
        """Test PolicyList
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PolicyList`
        """
        model = PolicyList()  # noqa: E501
        if include_optional:
            return PolicyList(
                pagination = lakefs_sdk_async.models.pagination.Pagination(
                    has_more = True, 
                    next_offset = '', 
                    results = 0, 
                    max_per_page = 0, ),
                results = [
                    lakefs_sdk_async.models.policy.Policy(
                        id = '', 
                        creation_date = 56, 
                        statement = [
                            lakefs_sdk_async.models.statement.Statement(
                                effect = 'allow', 
                                resource = '', 
                                action = [
                                    ''
                                    ], )
                            ], )
                    ]
            )
        else:
            return PolicyList(
                pagination = lakefs_sdk_async.models.pagination.Pagination(
                    has_more = True, 
                    next_offset = '', 
                    results = 0, 
                    max_per_page = 0, ),
                results = [
                    lakefs_sdk_async.models.policy.Policy(
                        id = '', 
                        creation_date = 56, 
                        statement = [
                            lakefs_sdk_async.models.statement.Statement(
                                effect = 'allow', 
                                resource = '', 
                                action = [
                                    ''
                                    ], )
                            ], )
                    ],
        )
        """

    def testPolicyList(self):
        """Test PolicyList"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
