# -*- coding: utf-8 -*-

import requests
import unittest
from jsonrpclient import JSONRPCClient
from jsonrpclient import InvalidRequestError, ServerError


class JsonRPCClientTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.url = 'http://localhost:4000/'
        cls.client = JSONRPCClient(cls.url)

    def test_init(self):
        client = JSONRPCClient(self.url)
        session = client.session
        self.assertTrue(isinstance(session, requests.sessions.Session))

        session = requests.Session()
        client = JSONRPCClient(self.url, session)
        self.assertEqual(id(client.session), id(session))

    def test_call_add(self):
        a, b = 10, 5
        json = self.client.add(a, b)
        self.assertEqual(a+b, json.get('result'))

        json = self.client.call('add', a, b)
        self.assertEqual(a+b, json.get('result'))

    def test_call_foobar(self):
        json = self.client.foobar(foo='hello', bar=' world')
        self.assertEqual('hello world', json.get('result'))

    def test_call_echo(self):
        json = self.client.echo("hello")
        self.assertEqual("hello", json.get('result'))

    def test_raise_exception(self):
        with self.assertRaises(InvalidRequestError):
            self.client.add('a', 'b', 'c')

    def test_notify(self):
        with self.assertRaises(ServerError):
            self.client.notify("echo", "hello", "world")
