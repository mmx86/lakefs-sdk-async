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

from lakefs_sdk_async.models.login_config import LoginConfig  # noqa: E501

class TestLoginConfig(unittest.TestCase):
    """LoginConfig unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> LoginConfig:
        """Test LoginConfig
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `LoginConfig`
        """
        model = LoginConfig()  # noqa: E501
        if include_optional:
            return LoginConfig(
                rbac = 'none',
                username_ui_placeholder = '',
                password_ui_placeholder = '',
                login_url = '',
                login_failed_message = '',
                fallback_login_url = '',
                fallback_login_label = '',
                login_cookie_names = [
                    ''
                    ],
                logout_url = ''
            )
        else:
            return LoginConfig(
                login_url = '',
                login_cookie_names = [
                    ''
                    ],
                logout_url = '',
        )
        """

    def testLoginConfig(self):
        """Test LoginConfig"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
