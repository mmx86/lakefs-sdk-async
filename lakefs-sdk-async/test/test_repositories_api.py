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
from lakefs_sdk_async.api.repositories_api import RepositoriesApi  # noqa: E501
from lakefs_sdk_async.rest import ApiException


class TestRepositoriesApi(unittest.TestCase):
    """RepositoriesApi unit test stubs"""

    def setUp(self):
        self.api = lakefs_sdk_async.api.repositories_api.RepositoriesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_repository(self):
        """Test case for create_repository

        create repository  # noqa: E501
        """
        pass

    def test_delete_gc_rules(self):
        """Test case for delete_gc_rules

        """
        pass

    def test_delete_repository(self):
        """Test case for delete_repository

        delete repository  # noqa: E501
        """
        pass

    def test_dump_status(self):
        """Test case for dump_status

        Status of a repository dump task  # noqa: E501
        """
        pass

    def test_dump_submit(self):
        """Test case for dump_submit

        Backup the repository metadata (tags, commits, branches) and save the backup to the object store.  # noqa: E501
        """
        pass

    def test_get_branch_protection_rules(self):
        """Test case for get_branch_protection_rules

        get branch protection rules  # noqa: E501
        """
        pass

    def test_get_gc_rules(self):
        """Test case for get_gc_rules

        get repository GC rules  # noqa: E501
        """
        pass

    def test_get_repository(self):
        """Test case for get_repository

        get repository  # noqa: E501
        """
        pass

    def test_get_repository_metadata(self):
        """Test case for get_repository_metadata

        get repository metadata  # noqa: E501
        """
        pass

    def test_list_repositories(self):
        """Test case for list_repositories

        list repositories  # noqa: E501
        """
        pass

    def test_restore_status(self):
        """Test case for restore_status

        Status of a restore request  # noqa: E501
        """
        pass

    def test_restore_submit(self):
        """Test case for restore_submit

        Restore repository from a dump in the object store  # noqa: E501
        """
        pass

    def test_set_branch_protection_rules(self):
        """Test case for set_branch_protection_rules

        """
        pass

    def test_set_gc_rules(self):
        """Test case for set_gc_rules

        """
        pass


if __name__ == '__main__':
    unittest.main()
