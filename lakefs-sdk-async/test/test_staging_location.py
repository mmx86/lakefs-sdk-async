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

from lakefs_sdk_async.models.staging_location import StagingLocation  # noqa: E501

class TestStagingLocation(unittest.TestCase):
    """StagingLocation unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> StagingLocation:
        """Test StagingLocation
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `StagingLocation`
        """
        model = StagingLocation()  # noqa: E501
        if include_optional:
            return StagingLocation(
                physical_address = '',
                presigned_url = '',
                presigned_url_expiry = 56
            )
        else:
            return StagingLocation(
        )
        """

    def testStagingLocation(self):
        """Test StagingLocation"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
