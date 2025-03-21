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
from lakefs_sdk_async.api.experimental_api import ExperimentalApi  # noqa: E501
from lakefs_sdk_async.rest import ApiException


class TestExperimentalApi(unittest.TestCase):
    """ExperimentalApi unit test stubs"""

    def setUp(self):
        self.api = lakefs_sdk_async.api.experimental_api.ExperimentalApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_abort_presign_multipart_upload(self):
        """Test case for abort_presign_multipart_upload

        Abort a presign multipart upload  # noqa: E501
        """
        pass

    def test_complete_presign_multipart_upload(self):
        """Test case for complete_presign_multipart_upload

        Complete a presign multipart upload request  # noqa: E501
        """
        pass

    def test_create_presign_multipart_upload(self):
        """Test case for create_presign_multipart_upload

        Initiate a multipart upload  # noqa: E501
        """
        pass

    def test_create_user_external_principal(self):
        """Test case for create_user_external_principal

        attach external principal to user  # noqa: E501
        """
        pass

    def test_delete_user_external_principal(self):
        """Test case for delete_user_external_principal

        delete external principal from user  # noqa: E501
        """
        pass

    def test_get_external_principal(self):
        """Test case for get_external_principal

        describe external principal by id  # noqa: E501
        """
        pass

    def test_hard_reset_branch(self):
        """Test case for hard_reset_branch

        hard reset branch  # noqa: E501
        """
        pass

    def test_list_user_external_principals(self):
        """Test case for list_user_external_principals

        list user external policies attached to a user  # noqa: E501
        """
        pass

    def test_s_ts_login(self):
        """Test case for s_ts_login

        perform a login with STS  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
