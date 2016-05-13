# -*- coding: utf-8 -*-


class ParseError(Exception):
    """
    Parse error Invalid JSON was received by the server.
    An error occurred on the server while parsing the JSON text.
    """
    pass


class InvalidRequestError(Exception):
    """
    Invalid Request The JSON sent is not a valid Request object.
    """
    pass


class MethodNotFound(Exception):
    """
    The method does not exist / is not available.
    """
    pass


class InvalidParamsError(Exception):
    """
    Invalid method parameter(s).
    """
    pass


class InternalError(Exception):
    """
    Internal JSON-RPC error.
    """
    pass


class ServerError(Exception):
    """
    Reserved for implementation-defined server-errors.
    """
    pass
