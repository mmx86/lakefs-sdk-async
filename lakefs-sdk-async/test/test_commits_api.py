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

from lakefs_sdk_async.api.commits_api import CommitsApi  # noqa: E501


class TestCommitsApi(unittest.TestCase):
    """CommitsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = CommitsApi()  # noqa: E501

    def tearDown(self) -> None:
        pass

    def test_commit(self) -> None:
        """Test case for commit

        create commit  # noqa: E501
        """
        pass

    def test_get_commit(self) -> None:
        """Test case for get_commit

        get commit  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
