# -*- coding: utf-8 -*-

import requests
from .handler import status_checker, json_checker
from .error import ParseError


class JSONRPCClient(object):

    def __init__(self, url, session=None, **kwargs):
        self.url = url
        self.response_handlers = [status_checker]
        self.json_handlers = [json_checker]
        self.rpc_id = 0
        self.session = session if session else requests.Session()

        self.interceptor = None
        self.kwargs = kwargs.copy()

    def call(self, method, *args, **kwargs):
        return self._call_json_rpc(method, False, *args, **kwargs)

    def notify(self, method, *args, **kwargs):
        return self._call_json_rpc(method, True, *args, **kwargs)

    def _call_json_rpc(self, method, is_notification=False, *args, **kwargs):
        if all((args, kwargs)):
            raise ValueError('call rpc method with positional parameters or named parameters')

        params = args if args else kwargs
        payload = dict(method=method, jsonrpc='2.0', params=params, id=self.rpc_id)
        if is_notification:
            payload.pop('id', None)

        response = self.session.post(self.url, json=payload, **self.kwargs)
        response.raise_for_status()

        for handler in self.response_handlers:
            handler(response)
        try:
            resp_json = response.json()
        except ValueError:
            raise ParseError('invalid JSON-RPC response')
        else:
            for handler in self.json_handlers:
                handler(resp_json)

            if self.interceptor is None:
                return resp_json
            else:
                return self.interceptor(response, resp_json)

    def __getattr__(self, item):
        def method(*args, **kwargs):
            return self.call(item, *args, **kwargs)
        return method
