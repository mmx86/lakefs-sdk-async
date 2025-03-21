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

import lakefs_sdk_async
from lakefs_sdk_async.api.tags_api import TagsApi  # noqa: E501
from lakefs_sdk_async.rest import ApiException


class TestTagsApi(unittest.TestCase):
    """TagsApi unit test stubs"""

    def setUp(self):
        self.api = lakefs_sdk_async.api.tags_api.TagsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_tag(self):
        """Test case for create_tag

        create tag  # noqa: E501
        """
        pass

    def test_delete_tag(self):
        """Test case for delete_tag

        delete tag  # noqa: E501
        """
        pass

    def test_get_tag(self):
        """Test case for get_tag

        get tag  # noqa: E501
        """
        pass

    def test_list_tags(self):
        """Test case for list_tags

        list tags  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
