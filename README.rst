jsonrpclient
============

Example
-------

::

    >>> from jsonrpclient import JSONRPCClient
    >>> client = JsonRPCClient("http://localhost:4000")
    >>> client.echo("hello world")
    {u'jsonrpc': u'2.0', u'result': u'hello world', u'id': 1}