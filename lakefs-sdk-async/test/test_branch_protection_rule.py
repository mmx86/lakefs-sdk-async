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

from lakefs_sdk_async.models.branch_protection_rule import BranchProtectionRule  # noqa: E501

class TestBranchProtectionRule(unittest.TestCase):
    """BranchProtectionRule unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> BranchProtectionRule:
        """Test BranchProtectionRule
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `BranchProtectionRule`
        """
        model = BranchProtectionRule()  # noqa: E501
        if include_optional:
            return BranchProtectionRule(
                pattern = 'stable_*'
            )
        else:
            return BranchProtectionRule(
                pattern = 'stable_*',
        )
        """

    def testBranchProtectionRule(self):
        """Test BranchProtectionRule"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
