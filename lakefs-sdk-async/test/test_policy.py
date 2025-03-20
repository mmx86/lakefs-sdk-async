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
from lakefs_sdk_async.models.policy import Policy  # noqa: E501
from lakefs_sdk_async.rest import ApiException

class TestPolicy(unittest.TestCase):
    """Policy unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Policy
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Policy`
        """
        model = lakefs_sdk_async.models.policy.Policy()  # noqa: E501
        if include_optional :
            return Policy(
                id = '', 
                creation_date = 56, 
                statement = [
                    lakefs_sdk_async.models.statement.Statement(
                        effect = 'allow', 
                        resource = '', 
                        action = [
                            ''
                            ], )
                    ]
            )
        else :
            return Policy(
                id = '',
                statement = [
                    lakefs_sdk_async.models.statement.Statement(
                        effect = 'allow', 
                        resource = '', 
                        action = [
                            ''
                            ], )
                    ],
        )
        """

    def testPolicy(self):
        """Test Policy"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
