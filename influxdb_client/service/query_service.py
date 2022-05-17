# coding: utf-8

"""
InfluxDB OSS API Service.

The InfluxDB v2 API provides a programmatic interface for all interactions with InfluxDB. Access the InfluxDB API using the `/api/v2/` endpoint.   # noqa: E501

OpenAPI spec version: 2.0.0
Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

from influxdb_client.service._base_service import _BaseService


class QueryService(_BaseService):
    """NOTE: This class is auto generated by OpenAPI Generator.

    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):  # noqa: E501,D401,D403
        """QueryService - a operation defined in OpenAPI."""
        if api_client is None:
            raise ValueError("Invalid value for `api_client`, must be defined.")
        self.api_client = api_client

    def get_query_suggestions(self, **kwargs):  # noqa: E501,D401,D403
        """Retrieve query suggestions.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_query_suggestions(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str zap_trace_span: OpenTracing span context
        :return: FluxSuggestions
                 If the method is called asynchronously,
                 returns the request thread.
        """  # noqa: E501
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_query_suggestions_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_query_suggestions_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_query_suggestions_with_http_info(self, **kwargs):  # noqa: E501,D401,D403
        """Retrieve query suggestions.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_query_suggestions_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str zap_trace_span: OpenTracing span context
        :return: FluxSuggestions
                 If the method is called asynchronously,
                 returns the request thread.
        """  # noqa: E501
        local_var_params, path_params, query_params, header_params, body_params = \
            self._get_query_suggestions_prepare(**kwargs)

        return self.api_client.call_api(
            '/api/v2/query/suggestions', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=[],
            files={},
            response_type='FluxSuggestions',  # noqa: E501
            auth_settings=[],
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats={},
            urlopen_kw=kwargs.get('urlopen_kw', None))

    async def get_query_suggestions_async(self, **kwargs):  # noqa: E501,D401,D403
        """Retrieve query suggestions.

        This method makes an asynchronous HTTP request.

        :param async_req bool
        :param str zap_trace_span: OpenTracing span context
        :return: FluxSuggestions
                 If the method is called asynchronously,
                 returns the request thread.
        """  # noqa: E501
        local_var_params, path_params, query_params, header_params, body_params = \
            self._get_query_suggestions_prepare(**kwargs)

        return await self.api_client.call_api(
            '/api/v2/query/suggestions', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=[],
            files={},
            response_type='FluxSuggestions',  # noqa: E501
            auth_settings=[],
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats={},
            urlopen_kw=kwargs.get('urlopen_kw', None))

    def _get_query_suggestions_prepare(self, **kwargs):  # noqa: E501,D401,D403
        local_var_params = locals()

        all_params = ['zap_trace_span']  # noqa: E501
        self._check_operation_params('get_query_suggestions', all_params, local_var_params)

        path_params = {}

        query_params = []

        header_params = {}
        if 'zap_trace_span' in local_var_params:
            header_params['Zap-Trace-Span'] = local_var_params['zap_trace_span']  # noqa: E501

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        return local_var_params, path_params, query_params, header_params, body_params

    def get_query_suggestions_name(self, name, **kwargs):  # noqa: E501,D401,D403
        """Retrieve query suggestions for a branching suggestion.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_query_suggestions_name(name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str name: The name of the branching suggestion. (required)
        :param str zap_trace_span: OpenTracing span context
        :return: FluxSuggestion
                 If the method is called asynchronously,
                 returns the request thread.
        """  # noqa: E501
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_query_suggestions_name_with_http_info(name, **kwargs)  # noqa: E501
        else:
            (data) = self.get_query_suggestions_name_with_http_info(name, **kwargs)  # noqa: E501
            return data

    def get_query_suggestions_name_with_http_info(self, name, **kwargs):  # noqa: E501,D401,D403
        """Retrieve query suggestions for a branching suggestion.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_query_suggestions_name_with_http_info(name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str name: The name of the branching suggestion. (required)
        :param str zap_trace_span: OpenTracing span context
        :return: FluxSuggestion
                 If the method is called asynchronously,
                 returns the request thread.
        """  # noqa: E501
        local_var_params, path_params, query_params, header_params, body_params = \
            self._get_query_suggestions_name_prepare(name, **kwargs)

        return self.api_client.call_api(
            '/api/v2/query/suggestions/{name}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=[],
            files={},
            response_type='FluxSuggestion',  # noqa: E501
            auth_settings=[],
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats={},
            urlopen_kw=kwargs.get('urlopen_kw', None))

    async def get_query_suggestions_name_async(self, name, **kwargs):  # noqa: E501,D401,D403
        """Retrieve query suggestions for a branching suggestion.

        This method makes an asynchronous HTTP request.

        :param async_req bool
        :param str name: The name of the branching suggestion. (required)
        :param str zap_trace_span: OpenTracing span context
        :return: FluxSuggestion
                 If the method is called asynchronously,
                 returns the request thread.
        """  # noqa: E501
        local_var_params, path_params, query_params, header_params, body_params = \
            self._get_query_suggestions_name_prepare(name, **kwargs)

        return await self.api_client.call_api(
            '/api/v2/query/suggestions/{name}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=[],
            files={},
            response_type='FluxSuggestion',  # noqa: E501
            auth_settings=[],
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats={},
            urlopen_kw=kwargs.get('urlopen_kw', None))

    def _get_query_suggestions_name_prepare(self, name, **kwargs):  # noqa: E501,D401,D403
        local_var_params = locals()

        all_params = ['name', 'zap_trace_span']  # noqa: E501
        self._check_operation_params('get_query_suggestions_name', all_params, local_var_params)
        # verify the required parameter 'name' is set
        if ('name' not in local_var_params or
                local_var_params['name'] is None):
            raise ValueError("Missing the required parameter `name` when calling `get_query_suggestions_name`")  # noqa: E501

        path_params = {}
        if 'name' in local_var_params:
            path_params['name'] = local_var_params['name']  # noqa: E501

        query_params = []

        header_params = {}
        if 'zap_trace_span' in local_var_params:
            header_params['Zap-Trace-Span'] = local_var_params['zap_trace_span']  # noqa: E501

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        return local_var_params, path_params, query_params, header_params, body_params

    def post_query(self, **kwargs):  # noqa: E501,D401,D403
        """Query data.

        Retrieves data from buckets.  Use this endpoint to send a Flux query request and retreive data from a bucket.  #### Rate limits (with InfluxDB Cloud)  `read` rate limits apply. For more information, see [limits and adjustable quotas](https://docs.influxdata.com/influxdb/cloud/account-management/limits/).  #### Related guides  - [Query with the InfluxDB API](https://docs.influxdata.com/influxdb/v2.2/query-data/execute-queries/influx-api/). - [Get started with Flux](https://docs.influxdata.com/flux/v0.x/get-started/)
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_query(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str zap_trace_span: OpenTracing span context
        :param str accept_encoding: The content encoding (usually a compression algorithm) that the client can understand.
        :param str content_type:
        :param str org: The name or ID of the organization executing the query.  #### InfluxDB Cloud  - Doesn't use `org` or `orgID`. - Queries the bucket in the organization associated with the authorization (API token).  #### InfluxDB OSS  - Requires either `org` or `orgID`.
        :param str org_id: The ID of the organization executing the query.  #### InfluxDB Cloud  - Doesn't use `org` or `orgID`. - Queries the bucket in the organization associated with the authorization (API token).  #### InfluxDB OSS  - Requires either `org` or `orgID`.
        :param Query query: Flux query or specification to execute
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """  # noqa: E501
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.post_query_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.post_query_with_http_info(**kwargs)  # noqa: E501
            return data

    def post_query_with_http_info(self, **kwargs):  # noqa: E501,D401,D403
        """Query data.

        Retrieves data from buckets.  Use this endpoint to send a Flux query request and retreive data from a bucket.  #### Rate limits (with InfluxDB Cloud)  `read` rate limits apply. For more information, see [limits and adjustable quotas](https://docs.influxdata.com/influxdb/cloud/account-management/limits/).  #### Related guides  - [Query with the InfluxDB API](https://docs.influxdata.com/influxdb/v2.2/query-data/execute-queries/influx-api/). - [Get started with Flux](https://docs.influxdata.com/flux/v0.x/get-started/)
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_query_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str zap_trace_span: OpenTracing span context
        :param str accept_encoding: The content encoding (usually a compression algorithm) that the client can understand.
        :param str content_type:
        :param str org: The name or ID of the organization executing the query.  #### InfluxDB Cloud  - Doesn't use `org` or `orgID`. - Queries the bucket in the organization associated with the authorization (API token).  #### InfluxDB OSS  - Requires either `org` or `orgID`.
        :param str org_id: The ID of the organization executing the query.  #### InfluxDB Cloud  - Doesn't use `org` or `orgID`. - Queries the bucket in the organization associated with the authorization (API token).  #### InfluxDB OSS  - Requires either `org` or `orgID`.
        :param Query query: Flux query or specification to execute
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """  # noqa: E501
        local_var_params, path_params, query_params, header_params, body_params = \
            self._post_query_prepare(**kwargs)

        return self.api_client.call_api(
            '/api/v2/query', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=[],
            files={},
            response_type='str',  # noqa: E501
            auth_settings=[],
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats={},
            urlopen_kw=kwargs.get('urlopen_kw', None))

    async def post_query_async(self, **kwargs):  # noqa: E501,D401,D403
        """Query data.

        Retrieves data from buckets.  Use this endpoint to send a Flux query request and retreive data from a bucket.  #### Rate limits (with InfluxDB Cloud)  `read` rate limits apply. For more information, see [limits and adjustable quotas](https://docs.influxdata.com/influxdb/cloud/account-management/limits/).  #### Related guides  - [Query with the InfluxDB API](https://docs.influxdata.com/influxdb/v2.2/query-data/execute-queries/influx-api/). - [Get started with Flux](https://docs.influxdata.com/flux/v0.x/get-started/)
        This method makes an asynchronous HTTP request.

        :param async_req bool
        :param str zap_trace_span: OpenTracing span context
        :param str accept_encoding: The content encoding (usually a compression algorithm) that the client can understand.
        :param str content_type:
        :param str org: The name or ID of the organization executing the query.  #### InfluxDB Cloud  - Doesn't use `org` or `orgID`. - Queries the bucket in the organization associated with the authorization (API token).  #### InfluxDB OSS  - Requires either `org` or `orgID`.
        :param str org_id: The ID of the organization executing the query.  #### InfluxDB Cloud  - Doesn't use `org` or `orgID`. - Queries the bucket in the organization associated with the authorization (API token).  #### InfluxDB OSS  - Requires either `org` or `orgID`.
        :param Query query: Flux query or specification to execute
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """  # noqa: E501
        local_var_params, path_params, query_params, header_params, body_params = \
            self._post_query_prepare(**kwargs)

        return await self.api_client.call_api(
            '/api/v2/query', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=[],
            files={},
            response_type='str',  # noqa: E501
            auth_settings=[],
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats={},
            urlopen_kw=kwargs.get('urlopen_kw', None))

    def _post_query_prepare(self, **kwargs):  # noqa: E501,D401,D403
        local_var_params = locals()

        all_params = ['zap_trace_span', 'accept_encoding', 'content_type', 'org', 'org_id', 'query']  # noqa: E501
        self._check_operation_params('post_query', all_params, local_var_params)

        path_params = {}

        query_params = []
        if 'org' in local_var_params:
            query_params.append(('org', local_var_params['org']))  # noqa: E501
        if 'org_id' in local_var_params:
            query_params.append(('orgID', local_var_params['org_id']))  # noqa: E501

        header_params = {}
        if 'zap_trace_span' in local_var_params:
            header_params['Zap-Trace-Span'] = local_var_params['zap_trace_span']  # noqa: E501
        if 'accept_encoding' in local_var_params:
            header_params['Accept-Encoding'] = local_var_params['accept_encoding']  # noqa: E501
        if 'content_type' in local_var_params:
            header_params['Content-Type'] = local_var_params['content_type']  # noqa: E501

        body_params = None
        if 'query' in local_var_params:
            body_params = local_var_params['query']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/csv', 'application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'application/vnd.flux'])  # noqa: E501

        return local_var_params, path_params, query_params, header_params, body_params

    def post_query_analyze(self, **kwargs):  # noqa: E501,D401,D403
        """Analyze a Flux query.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_query_analyze(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str zap_trace_span: OpenTracing span context
        :param str content_type:
        :param Query query: Flux query to analyze
        :return: AnalyzeQueryResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """  # noqa: E501
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.post_query_analyze_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.post_query_analyze_with_http_info(**kwargs)  # noqa: E501
            return data

    def post_query_analyze_with_http_info(self, **kwargs):  # noqa: E501,D401,D403
        """Analyze a Flux query.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_query_analyze_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str zap_trace_span: OpenTracing span context
        :param str content_type:
        :param Query query: Flux query to analyze
        :return: AnalyzeQueryResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """  # noqa: E501
        local_var_params, path_params, query_params, header_params, body_params = \
            self._post_query_analyze_prepare(**kwargs)

        return self.api_client.call_api(
            '/api/v2/query/analyze', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=[],
            files={},
            response_type='AnalyzeQueryResponse',  # noqa: E501
            auth_settings=[],
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats={},
            urlopen_kw=kwargs.get('urlopen_kw', None))

    async def post_query_analyze_async(self, **kwargs):  # noqa: E501,D401,D403
        """Analyze a Flux query.

        This method makes an asynchronous HTTP request.

        :param async_req bool
        :param str zap_trace_span: OpenTracing span context
        :param str content_type:
        :param Query query: Flux query to analyze
        :return: AnalyzeQueryResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """  # noqa: E501
        local_var_params, path_params, query_params, header_params, body_params = \
            self._post_query_analyze_prepare(**kwargs)

        return await self.api_client.call_api(
            '/api/v2/query/analyze', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=[],
            files={},
            response_type='AnalyzeQueryResponse',  # noqa: E501
            auth_settings=[],
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats={},
            urlopen_kw=kwargs.get('urlopen_kw', None))

    def _post_query_analyze_prepare(self, **kwargs):  # noqa: E501,D401,D403
        local_var_params = locals()

        all_params = ['zap_trace_span', 'content_type', 'query']  # noqa: E501
        self._check_operation_params('post_query_analyze', all_params, local_var_params)

        path_params = {}

        query_params = []

        header_params = {}
        if 'zap_trace_span' in local_var_params:
            header_params['Zap-Trace-Span'] = local_var_params['zap_trace_span']  # noqa: E501
        if 'content_type' in local_var_params:
            header_params['Content-Type'] = local_var_params['content_type']  # noqa: E501

        body_params = None
        if 'query' in local_var_params:
            body_params = local_var_params['query']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        return local_var_params, path_params, query_params, header_params, body_params

    def post_query_ast(self, **kwargs):  # noqa: E501,D401,D403
        """Generate an Abstract Syntax Tree (AST) from a query.

        Analyzes flux query and generates a query specification.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_query_ast(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str zap_trace_span: OpenTracing span context
        :param str content_type:
        :param LanguageRequest language_request: Analyzed Flux query to generate abstract syntax tree.
        :return: ASTResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """  # noqa: E501
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.post_query_ast_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.post_query_ast_with_http_info(**kwargs)  # noqa: E501
            return data

    def post_query_ast_with_http_info(self, **kwargs):  # noqa: E501,D401,D403
        """Generate an Abstract Syntax Tree (AST) from a query.

        Analyzes flux query and generates a query specification.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_query_ast_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str zap_trace_span: OpenTracing span context
        :param str content_type:
        :param LanguageRequest language_request: Analyzed Flux query to generate abstract syntax tree.
        :return: ASTResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """  # noqa: E501
        local_var_params, path_params, query_params, header_params, body_params = \
            self._post_query_ast_prepare(**kwargs)

        return self.api_client.call_api(
            '/api/v2/query/ast', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=[],
            files={},
            response_type='ASTResponse',  # noqa: E501
            auth_settings=[],
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats={},
            urlopen_kw=kwargs.get('urlopen_kw', None))

    async def post_query_ast_async(self, **kwargs):  # noqa: E501,D401,D403
        """Generate an Abstract Syntax Tree (AST) from a query.

        Analyzes flux query and generates a query specification.
        This method makes an asynchronous HTTP request.

        :param async_req bool
        :param str zap_trace_span: OpenTracing span context
        :param str content_type:
        :param LanguageRequest language_request: Analyzed Flux query to generate abstract syntax tree.
        :return: ASTResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """  # noqa: E501
        local_var_params, path_params, query_params, header_params, body_params = \
            self._post_query_ast_prepare(**kwargs)

        return await self.api_client.call_api(
            '/api/v2/query/ast', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=[],
            files={},
            response_type='ASTResponse',  # noqa: E501
            auth_settings=[],
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats={},
            urlopen_kw=kwargs.get('urlopen_kw', None))

    def _post_query_ast_prepare(self, **kwargs):  # noqa: E501,D401,D403
        local_var_params = locals()

        all_params = ['zap_trace_span', 'content_type', 'language_request']  # noqa: E501
        self._check_operation_params('post_query_ast', all_params, local_var_params)

        path_params = {}

        query_params = []

        header_params = {}
        if 'zap_trace_span' in local_var_params:
            header_params['Zap-Trace-Span'] = local_var_params['zap_trace_span']  # noqa: E501
        if 'content_type' in local_var_params:
            header_params['Content-Type'] = local_var_params['content_type']  # noqa: E501

        body_params = None
        if 'language_request' in local_var_params:
            body_params = local_var_params['language_request']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        return local_var_params, path_params, query_params, header_params, body_params
