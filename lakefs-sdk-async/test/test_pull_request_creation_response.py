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

from lakefs_sdk_async.models.pull_request_creation_response import PullRequestCreationResponse  # noqa: E501

class TestPullRequestCreationResponse(unittest.TestCase):
    """PullRequestCreationResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PullRequestCreationResponse:
        """Test PullRequestCreationResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PullRequestCreationResponse`
        """
        model = PullRequestCreationResponse()  # noqa: E501
        if include_optional:
            return PullRequestCreationResponse(
                id = ''
            )
        else:
            return PullRequestCreationResponse(
                id = '',
        )
        """

    def testPullRequestCreationResponse(self):
        """Test PullRequestCreationResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
