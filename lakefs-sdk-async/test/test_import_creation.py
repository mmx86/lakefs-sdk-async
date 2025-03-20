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

from lakefs_sdk_async.models.import_creation import ImportCreation  # noqa: E501

class TestImportCreation(unittest.TestCase):
    """ImportCreation unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ImportCreation:
        """Test ImportCreation
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ImportCreation`
        """
        model = ImportCreation()  # noqa: E501
        if include_optional:
            return ImportCreation(
                paths = [
                    lakefs_sdk_async.models.import_location.ImportLocation(
                        type = 'common_prefix', 
                        path = 's3://my-bucket/production/collections/', 
                        destination = 'collections/', )
                    ],
                commit = lakefs_sdk_async.models.commit_creation.CommitCreation(
                    message = '', 
                    metadata = {
                        'key' : ''
                        }, 
                    date = 56, 
                    allow_empty = True, 
                    force = True, ),
                force = True
            )
        else:
            return ImportCreation(
                paths = [
                    lakefs_sdk_async.models.import_location.ImportLocation(
                        type = 'common_prefix', 
                        path = 's3://my-bucket/production/collections/', 
                        destination = 'collections/', )
                    ],
                commit = lakefs_sdk_async.models.commit_creation.CommitCreation(
                    message = '', 
                    metadata = {
                        'key' : ''
                        }, 
                    date = 56, 
                    allow_empty = True, 
                    force = True, ),
        )
        """

    def testImportCreation(self):
        """Test ImportCreation"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
