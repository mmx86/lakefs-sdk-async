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
from lakefs_sdk_async.api.internal_api import InternalApi  # noqa: E501
from lakefs_sdk_async.rest import ApiException


class TestInternalApi(unittest.TestCase):
    """InternalApi unit test stubs"""

    def setUp(self):
        self.api = lakefs_sdk_async.api.internal_api.InternalApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_branch_protection_rule_preflight(self):
        """Test case for create_branch_protection_rule_preflight

        """
        pass

    def test_create_symlink_file(self):
        """Test case for create_symlink_file

        creates symlink files corresponding to the given directory  # noqa: E501
        """
        pass

    def test_dump_refs(self):
        """Test case for dump_refs

        Dump repository refs (tags, commits, branches) to object store Deprecated: a new API will introduce long running operations   # noqa: E501
        """
        pass

    def test_get_auth_capabilities(self):
        """Test case for get_auth_capabilities

        list authentication capabilities supported  # noqa: E501
        """
        pass

    def test_get_garbage_collection_config(self):
        """Test case for get_garbage_collection_config

        """
        pass

    def test_get_lake_fs_version(self):
        """Test case for get_lake_fs_version

        """
        pass

    def test_get_setup_state(self):
        """Test case for get_setup_state

        check if the lakeFS installation is already set up  # noqa: E501
        """
        pass

    def test_get_storage_config(self):
        """Test case for get_storage_config

        """
        pass

    def test_internal_create_branch_protection_rule(self):
        """Test case for internal_create_branch_protection_rule

        """
        pass

    def test_internal_delete_branch_protection_rule(self):
        """Test case for internal_delete_branch_protection_rule

        """
        pass

    def test_internal_delete_garbage_collection_rules(self):
        """Test case for internal_delete_garbage_collection_rules

        """
        pass

    def test_internal_get_branch_protection_rules(self):
        """Test case for internal_get_branch_protection_rules

        get branch protection rules  # noqa: E501
        """
        pass

    def test_internal_get_garbage_collection_rules(self):
        """Test case for internal_get_garbage_collection_rules

        """
        pass

    def test_internal_set_garbage_collection_rules(self):
        """Test case for internal_set_garbage_collection_rules

        """
        pass

    def test_post_stats_events(self):
        """Test case for post_stats_events

        post stats events, this endpoint is meant for internal use only  # noqa: E501
        """
        pass

    def test_prepare_garbage_collection_commits(self):
        """Test case for prepare_garbage_collection_commits

        save lists of active commits for garbage collection  # noqa: E501
        """
        pass

    def test_prepare_garbage_collection_uncommitted(self):
        """Test case for prepare_garbage_collection_uncommitted

        save repository uncommitted metadata for garbage collection  # noqa: E501
        """
        pass

    def test_restore_refs(self):
        """Test case for restore_refs

        Restore repository refs (tags, commits, branches) from object store. Deprecated: a new API will introduce long running operations   # noqa: E501
        """
        pass

    def test_set_garbage_collection_rules_preflight(self):
        """Test case for set_garbage_collection_rules_preflight

        """
        pass

    def test_setup(self):
        """Test case for setup

        setup lakeFS and create a first user  # noqa: E501
        """
        pass

    def test_setup_comm_prefs(self):
        """Test case for setup_comm_prefs

        setup communications preferences  # noqa: E501
        """
        pass

    def test_stage_object(self):
        """Test case for stage_object

        stage an object's metadata for the given branch  # noqa: E501
        """
        pass

    def test_upload_object_preflight(self):
        """Test case for upload_object_preflight

        """
        pass


if __name__ == '__main__':
    unittest.main()
