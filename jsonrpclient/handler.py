# -*- coding: utf-8 -*-

from error import *
from requests.exceptions import HTTPError


_ERROR_CODE_MAP = {
    -32700: ParseError,
    -32600: InvalidRequestError,
    -32601: MethodNotFound,
    -32602: InvalidRequestError,
    -32603: InternalError,
}


def status_checker(resp):
    if 200 <= resp.status_code < 300:
        return True
    else:
        raise HTTPError("{}".format(resp.status_code))


def json_checker(json):
    error = json.get('error', None)
    if error is None:
        return True

    err_code = error.get('code', 0)
    err_msg = error.get('message', '')

    if err_code in _ERROR_CODE_MAP:
        raise _ERROR_CODE_MAP[err_code](err_msg)

    if -32099 <= err_code <= -32000:
        raise ServerError(err_msg)
    return False
