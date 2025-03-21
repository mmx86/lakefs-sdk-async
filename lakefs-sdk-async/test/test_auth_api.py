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
from lakefs_sdk_async.api.auth_api import AuthApi  # noqa: E501
from lakefs_sdk_async.rest import ApiException


class TestAuthApi(unittest.TestCase):
    """AuthApi unit test stubs"""

    def setUp(self):
        self.api = lakefs_sdk_async.api.auth_api.AuthApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_group_membership(self):
        """Test case for add_group_membership

        add group membership  # noqa: E501
        """
        pass

    def test_attach_policy_to_group(self):
        """Test case for attach_policy_to_group

        attach policy to group  # noqa: E501
        """
        pass

    def test_attach_policy_to_user(self):
        """Test case for attach_policy_to_user

        attach policy to user  # noqa: E501
        """
        pass

    def test_create_credentials(self):
        """Test case for create_credentials

        create credentials  # noqa: E501
        """
        pass

    def test_create_group(self):
        """Test case for create_group

        create group  # noqa: E501
        """
        pass

    def test_create_policy(self):
        """Test case for create_policy

        create policy  # noqa: E501
        """
        pass

    def test_create_user(self):
        """Test case for create_user

        create user  # noqa: E501
        """
        pass

    def test_create_user_external_principal(self):
        """Test case for create_user_external_principal

        attach external principal to user  # noqa: E501
        """
        pass

    def test_delete_credentials(self):
        """Test case for delete_credentials

        delete credentials  # noqa: E501
        """
        pass

    def test_delete_group(self):
        """Test case for delete_group

        delete group  # noqa: E501
        """
        pass

    def test_delete_group_membership(self):
        """Test case for delete_group_membership

        delete group membership  # noqa: E501
        """
        pass

    def test_delete_policy(self):
        """Test case for delete_policy

        delete policy  # noqa: E501
        """
        pass

    def test_delete_user(self):
        """Test case for delete_user

        delete user  # noqa: E501
        """
        pass

    def test_delete_user_external_principal(self):
        """Test case for delete_user_external_principal

        delete external principal from user  # noqa: E501
        """
        pass

    def test_detach_policy_from_group(self):
        """Test case for detach_policy_from_group

        detach policy from group  # noqa: E501
        """
        pass

    def test_detach_policy_from_user(self):
        """Test case for detach_policy_from_user

        detach policy from user  # noqa: E501
        """
        pass

    def test_get_credentials(self):
        """Test case for get_credentials

        get credentials  # noqa: E501
        """
        pass

    def test_get_current_user(self):
        """Test case for get_current_user

        get current user  # noqa: E501
        """
        pass

    def test_get_group(self):
        """Test case for get_group

        get group  # noqa: E501
        """
        pass

    def test_get_group_acl(self):
        """Test case for get_group_acl

        get ACL of group  # noqa: E501
        """
        pass

    def test_get_policy(self):
        """Test case for get_policy

        get policy  # noqa: E501
        """
        pass

    def test_get_user(self):
        """Test case for get_user

        get user  # noqa: E501
        """
        pass

    def test_get_user_external_principal(self):
        """Test case for get_user_external_principal

        get external principal of a user  # noqa: E501
        """
        pass

    def test_list_group_members(self):
        """Test case for list_group_members

        list group members  # noqa: E501
        """
        pass

    def test_list_group_policies(self):
        """Test case for list_group_policies

        list group policies  # noqa: E501
        """
        pass

    def test_list_groups(self):
        """Test case for list_groups

        list groups  # noqa: E501
        """
        pass

    def test_list_policies(self):
        """Test case for list_policies

        list policies  # noqa: E501
        """
        pass

    def test_list_user_credentials(self):
        """Test case for list_user_credentials

        list user credentials  # noqa: E501
        """
        pass

    def test_list_user_external_principals(self):
        """Test case for list_user_external_principals

        list user external policies attached to a user  # noqa: E501
        """
        pass

    def test_list_user_groups(self):
        """Test case for list_user_groups

        list user groups  # noqa: E501
        """
        pass

    def test_list_user_policies(self):
        """Test case for list_user_policies

        list user policies  # noqa: E501
        """
        pass

    def test_list_users(self):
        """Test case for list_users

        list users  # noqa: E501
        """
        pass

    def test_login(self):
        """Test case for login

        perform a login  # noqa: E501
        """
        pass

    def test_set_group_acl(self):
        """Test case for set_group_acl

        set ACL of group  # noqa: E501
        """
        pass

    def test_update_policy(self):
        """Test case for update_policy

        update policy  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
