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

from lakefs_sdk_async.models.import_location import ImportLocation  # noqa: E501

class TestImportLocation(unittest.TestCase):
    """ImportLocation unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ImportLocation:
        """Test ImportLocation
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ImportLocation`
        """
        model = ImportLocation()  # noqa: E501
        if include_optional:
            return ImportLocation(
                type = 'common_prefix',
                path = 's3://my-bucket/production/collections/',
                destination = 'collections/'
            )
        else:
            return ImportLocation(
                type = 'common_prefix',
                path = 's3://my-bucket/production/collections/',
                destination = 'collections/',
        )
        """

    def testImportLocation(self):
        """Test ImportLocation"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
