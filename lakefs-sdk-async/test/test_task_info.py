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

from lakefs_sdk_async.models.task_info import TaskInfo  # noqa: E501

class TestTaskInfo(unittest.TestCase):
    """TaskInfo unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TaskInfo:
        """Test TaskInfo
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TaskInfo`
        """
        model = TaskInfo()  # noqa: E501
        if include_optional:
            return TaskInfo(
                id = ''
            )
        else:
            return TaskInfo(
                id = '',
        )
        """

    def testTaskInfo(self):
        """Test TaskInfo"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
