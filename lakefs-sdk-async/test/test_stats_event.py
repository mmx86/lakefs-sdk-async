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
from lakefs_sdk_async.models.stats_event import StatsEvent  # noqa: E501
from lakefs_sdk_async.rest import ApiException

class TestStatsEvent(unittest.TestCase):
    """StatsEvent unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test StatsEvent
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `StatsEvent`
        """
        model = lakefs_sdk_async.models.stats_event.StatsEvent()  # noqa: E501
        if include_optional :
            return StatsEvent(
                var_class = '', 
                name = '', 
                count = 56
            )
        else :
            return StatsEvent(
                var_class = '',
                name = '',
                count = 56,
        )
        """

    def testStatsEvent(self):
        """Test StatsEvent"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
