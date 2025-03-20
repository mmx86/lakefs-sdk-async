# coding: utf-8

"""
    lakeFS API

    lakeFS HTTP API

    The version of the OpenAPI document: 1.0.0
    Contact: services@treeverse.io
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import re  # noqa: F401
import io
import warnings

try:
    from pydantic.v1 import validate_arguments, ValidationError
except ImportError:
    from pydantic import validate_arguments, ValidationError
from typing_extensions import Annotated
from typing import overload, Optional, Union, Awaitable

try:
    from pydantic.v1 import Field, StrictStr, conint
except ImportError:
    from pydantic import Field, StrictStr, conint

from typing import Optional

from lakefs_sdk_async.models.pull_request import PullRequest
from lakefs_sdk_async.models.pull_request_basic import PullRequestBasic
from lakefs_sdk_async.models.pull_request_creation import PullRequestCreation
from lakefs_sdk_async.models.pull_requests_list import PullRequestsList

from lakefs_sdk_async.api_client import ApiClient
from lakefs_sdk_async.api_response import ApiResponse
from lakefs_sdk_async.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class PullsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client

    @overload
    async def create_pull_request(self, repository : StrictStr, pull_request_creation : PullRequestCreation, **kwargs) -> str:  # noqa: E501
        ...

    @overload
    def create_pull_request(self, repository : StrictStr, pull_request_creation : PullRequestCreation, async_req: Optional[bool]=True, **kwargs) -> str:  # noqa: E501
        ...

    @validate_arguments
    def create_pull_request(self, repository : StrictStr, pull_request_creation : PullRequestCreation, async_req: Optional[bool]=None, **kwargs) -> Union[str, Awaitable[str]]:  # noqa: E501
        """create pull request  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_pull_request(repository, pull_request_creation, async_req=True)
        >>> result = thread.get()

        :param repository: (required)
        :type repository: str
        :param pull_request_creation: (required)
        :type pull_request_creation: PullRequestCreation
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: str
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the create_pull_request_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        if async_req is not None:
            kwargs['async_req'] = async_req
        return self.create_pull_request_with_http_info(repository, pull_request_creation, **kwargs)  # noqa: E501

    @validate_arguments
    def create_pull_request_with_http_info(self, repository : StrictStr, pull_request_creation : PullRequestCreation, **kwargs) -> ApiResponse:  # noqa: E501
        """create pull request  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_pull_request_with_http_info(repository, pull_request_creation, async_req=True)
        >>> result = thread.get()

        :param repository: (required)
        :type repository: str
        :param pull_request_creation: (required)
        :type pull_request_creation: PullRequestCreation
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the 
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(str, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'repository',
            'pull_request_creation'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_pull_request" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['repository']:
            _path_params['repository'] = _params['repository']


        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        if _params['pull_request_creation'] is not None:
            _body_params = _params['pull_request_creation']

        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['text/html', 'application/json'])  # noqa: E501

        # set the HTTP header `Content-Type`
        _content_types_list = _params.get('_content_type',
            self.api_client.select_header_content_type(
                ['application/json']))
        if _content_types_list:
                _header_params['Content-Type'] = _content_types_list

        # authentication setting
        _auth_settings = ['basic_auth', 'cookie_auth', 'oidc_auth', 'saml_auth', 'jwt_token']  # noqa: E501

        _response_types_map = {
            '201': "str",
            '400': "Error",
            '401': "Error",
            '403': "Error",
            '404': "Error",
            '409': "Error",
            '420': None,
        }

        return self.api_client.call_api(
            '/repositories/{repository}/pulls', 'POST',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @overload
    async def get_pull_request(self, repository : StrictStr, pull_request : Annotated[StrictStr, Field(..., description="pull request id")], **kwargs) -> PullRequest:  # noqa: E501
        ...

    @overload
    def get_pull_request(self, repository : StrictStr, pull_request : Annotated[StrictStr, Field(..., description="pull request id")], async_req: Optional[bool]=True, **kwargs) -> PullRequest:  # noqa: E501
        ...

    @validate_arguments
    def get_pull_request(self, repository : StrictStr, pull_request : Annotated[StrictStr, Field(..., description="pull request id")], async_req: Optional[bool]=None, **kwargs) -> Union[PullRequest, Awaitable[PullRequest]]:  # noqa: E501
        """get pull request  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_pull_request(repository, pull_request, async_req=True)
        >>> result = thread.get()

        :param repository: (required)
        :type repository: str
        :param pull_request: pull request id (required)
        :type pull_request: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: PullRequest
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the get_pull_request_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        if async_req is not None:
            kwargs['async_req'] = async_req
        return self.get_pull_request_with_http_info(repository, pull_request, **kwargs)  # noqa: E501

    @validate_arguments
    def get_pull_request_with_http_info(self, repository : StrictStr, pull_request : Annotated[StrictStr, Field(..., description="pull request id")], **kwargs) -> ApiResponse:  # noqa: E501
        """get pull request  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_pull_request_with_http_info(repository, pull_request, async_req=True)
        >>> result = thread.get()

        :param repository: (required)
        :type repository: str
        :param pull_request: pull request id (required)
        :type pull_request: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the 
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(PullRequest, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'repository',
            'pull_request'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_pull_request" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['repository']:
            _path_params['repository'] = _params['repository']

        if _params['pull_request']:
            _path_params['pull_request'] = _params['pull_request']


        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # authentication setting
        _auth_settings = ['basic_auth', 'cookie_auth', 'oidc_auth', 'saml_auth', 'jwt_token']  # noqa: E501

        _response_types_map = {
            '200': "PullRequest",
            '400': "Error",
            '401': "Error",
            '404': "Error",
            '420': None,
        }

        return self.api_client.call_api(
            '/repositories/{repository}/pulls/{pull_request}', 'GET',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @overload
    async def list_pull_requests(self, repository : StrictStr, prefix : Annotated[Optional[StrictStr], Field(description="return items prefixed with this value")] = None, after : Annotated[Optional[StrictStr], Field(description="return items after this value")] = None, amount : Annotated[Optional[conint(strict=True, le=1000, ge=-1)], Field(description="how many items to return")] = None, status : Optional[StrictStr] = None, **kwargs) -> PullRequestsList:  # noqa: E501
        ...

    @overload
    def list_pull_requests(self, repository : StrictStr, prefix : Annotated[Optional[StrictStr], Field(description="return items prefixed with this value")] = None, after : Annotated[Optional[StrictStr], Field(description="return items after this value")] = None, amount : Annotated[Optional[conint(strict=True, le=1000, ge=-1)], Field(description="how many items to return")] = None, status : Optional[StrictStr] = None, async_req: Optional[bool]=True, **kwargs) -> PullRequestsList:  # noqa: E501
        ...

    @validate_arguments
    def list_pull_requests(self, repository : StrictStr, prefix : Annotated[Optional[StrictStr], Field(description="return items prefixed with this value")] = None, after : Annotated[Optional[StrictStr], Field(description="return items after this value")] = None, amount : Annotated[Optional[conint(strict=True, le=1000, ge=-1)], Field(description="how many items to return")] = None, status : Optional[StrictStr] = None, async_req: Optional[bool]=None, **kwargs) -> Union[PullRequestsList, Awaitable[PullRequestsList]]:  # noqa: E501
        """list pull requests  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.list_pull_requests(repository, prefix, after, amount, status, async_req=True)
        >>> result = thread.get()

        :param repository: (required)
        :type repository: str
        :param prefix: return items prefixed with this value
        :type prefix: str
        :param after: return items after this value
        :type after: str
        :param amount: how many items to return
        :type amount: int
        :param status:
        :type status: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: PullRequestsList
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the list_pull_requests_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        if async_req is not None:
            kwargs['async_req'] = async_req
        return self.list_pull_requests_with_http_info(repository, prefix, after, amount, status, **kwargs)  # noqa: E501

    @validate_arguments
    def list_pull_requests_with_http_info(self, repository : StrictStr, prefix : Annotated[Optional[StrictStr], Field(description="return items prefixed with this value")] = None, after : Annotated[Optional[StrictStr], Field(description="return items after this value")] = None, amount : Annotated[Optional[conint(strict=True, le=1000, ge=-1)], Field(description="how many items to return")] = None, status : Optional[StrictStr] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """list pull requests  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.list_pull_requests_with_http_info(repository, prefix, after, amount, status, async_req=True)
        >>> result = thread.get()

        :param repository: (required)
        :type repository: str
        :param prefix: return items prefixed with this value
        :type prefix: str
        :param after: return items after this value
        :type after: str
        :param amount: how many items to return
        :type amount: int
        :param status:
        :type status: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the 
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(PullRequestsList, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'repository',
            'prefix',
            'after',
            'amount',
            'status'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_pull_requests" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['repository']:
            _path_params['repository'] = _params['repository']


        # process the query parameters
        _query_params = []
        if _params.get('prefix') is not None:  # noqa: E501
            _query_params.append(('prefix', _params['prefix']))

        if _params.get('after') is not None:  # noqa: E501
            _query_params.append(('after', _params['after']))

        if _params.get('amount') is not None:  # noqa: E501
            _query_params.append(('amount', _params['amount']))

        if _params.get('status') is not None:  # noqa: E501
            _query_params.append(('status', _params['status']))

        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # authentication setting
        _auth_settings = ['basic_auth', 'cookie_auth', 'oidc_auth', 'saml_auth', 'jwt_token']  # noqa: E501

        _response_types_map = {
            '200': "PullRequestsList",
            '401': "Error",
            '404': "Error",
            '420': None,
        }

        return self.api_client.call_api(
            '/repositories/{repository}/pulls', 'GET',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @overload
    async def update_pull_request(self, repository : StrictStr, pull_request : Annotated[StrictStr, Field(..., description="pull request id")], pull_request_basic : PullRequestBasic, **kwargs) -> None:  # noqa: E501
        ...

    @overload
    def update_pull_request(self, repository : StrictStr, pull_request : Annotated[StrictStr, Field(..., description="pull request id")], pull_request_basic : PullRequestBasic, async_req: Optional[bool]=True, **kwargs) -> None:  # noqa: E501
        ...

    @validate_arguments
    def update_pull_request(self, repository : StrictStr, pull_request : Annotated[StrictStr, Field(..., description="pull request id")], pull_request_basic : PullRequestBasic, async_req: Optional[bool]=None, **kwargs) -> Union[None, Awaitable[None]]:  # noqa: E501
        """update pull request  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.update_pull_request(repository, pull_request, pull_request_basic, async_req=True)
        >>> result = thread.get()

        :param repository: (required)
        :type repository: str
        :param pull_request: pull request id (required)
        :type pull_request: str
        :param pull_request_basic: (required)
        :type pull_request_basic: PullRequestBasic
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: None
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the update_pull_request_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        if async_req is not None:
            kwargs['async_req'] = async_req
        return self.update_pull_request_with_http_info(repository, pull_request, pull_request_basic, **kwargs)  # noqa: E501

    @validate_arguments
    def update_pull_request_with_http_info(self, repository : StrictStr, pull_request : Annotated[StrictStr, Field(..., description="pull request id")], pull_request_basic : PullRequestBasic, **kwargs) -> ApiResponse:  # noqa: E501
        """update pull request  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.update_pull_request_with_http_info(repository, pull_request, pull_request_basic, async_req=True)
        >>> result = thread.get()

        :param repository: (required)
        :type repository: str
        :param pull_request: pull request id (required)
        :type pull_request: str
        :param pull_request_basic: (required)
        :type pull_request_basic: PullRequestBasic
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the 
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: None
        """

        _params = locals()

        _all_params = [
            'repository',
            'pull_request',
            'pull_request_basic'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_pull_request" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['repository']:
            _path_params['repository'] = _params['repository']

        if _params['pull_request']:
            _path_params['pull_request'] = _params['pull_request']


        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        if _params['pull_request_basic'] is not None:
            _body_params = _params['pull_request_basic']

        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # set the HTTP header `Content-Type`
        _content_types_list = _params.get('_content_type',
            self.api_client.select_header_content_type(
                ['application/json']))
        if _content_types_list:
                _header_params['Content-Type'] = _content_types_list

        # authentication setting
        _auth_settings = ['basic_auth', 'cookie_auth', 'oidc_auth', 'saml_auth', 'jwt_token']  # noqa: E501

        _response_types_map = {}

        return self.api_client.call_api(
            '/repositories/{repository}/pulls/{pull_request}', 'PATCH',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))
