# -*- coding: utf-8 -*-

import requests
from .handler import status_checker, json_checker
from .error import ParseError

try:
    import simplejson as json
except (ImportError, SyntaxError):
    import json


class JsonRPCClient(object):

    def __init__(self, url, session=None, encoding='utf-8', rid=1, **kwargs):
        self.url = url
        self.response_handlers = [status_checker]
        self.json_handlers = [json_checker]
        self.encoding = encoding
        self.rpc_id = rid
        self.session = session if session else requests.session()
        self.session.headers['content-type'] = 'application/json;' \
                                               ' charset=%s' % encoding
        self.intercept_func = None
        self.kwargs = kwargs

    def call(self, method, *args, **kwargs):
        return _Method(self, method)(*args, **kwargs)

    def notify(self, method, *args, **kwargs):
        return _Method(self, method, is_notification=True)(*args, **kwargs)

    def __getattr__(self, method):
        return _Method(self, method)


class _Method(object):
    def __init__(self, client, method, is_notification=False):
        self.client = client
        self.method = method
        self.is_notification = is_notification

    def __call__(self, *args, **kwargs):
        if all((args, kwargs)):
            raise ValueError('call rpc method with positional parameters '
                             'or named parameters')
        client = self.client
        params = args if args else kwargs
        payload = dict(method=self.method, jsonrpc='2.0', params=params,
                       id=client.rpc_id)
        if self.is_notification:
            payload.pop('id', None)

        response = client.session.post(client.url, data=json.dumps(payload),
                                       **client.kwargs)

        for handler in client.response_handlers:
            handler(response)
        try:
            resp_json = response.json()
        except ValueError:
            raise ParseError('invalid JSON-RPC response')
        else:
            for handler in client.json_handlers:
                handler(resp_json)

            if client.intercept_func is None:
                return resp_json
            else:
                return client.hijack_func(response, resp_json)
