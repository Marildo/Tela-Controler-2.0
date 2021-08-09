import logging
from functools import wraps

from flask import request
from werkzeug.exceptions import UnprocessableEntity

from exceptions import DataBaseException, EntityNotFound

status_code = [100, 101, 102, 200, 201, 202, 203, 204, 205, 206, 207, 208, 226, 300, 301, 302, 303, 304, 305, 307, 308,
               400, 401, 402, 403, 404, 405, 406, 407, 408, 409, 410, 411, 412, 413, 414, 415, 416, 417, 418, 421, 422,
               423, 424, 426, 428, 429, 431, 444, 451, 499, 500, 501, 502, 503, 504, 505, 506, 507, 508, 510, 511, 599]


def is_status_code(code: int):
    result = code in status_code
    if not result:
        log_error(f'{code} is not status code')
    return result


def log_error(msg):
    error = {
        'msg': msg,
        'path': request.path,
        'method': request.method,
        'data': request.data
    }
    logging.error(error)


class Response:

    def __init__(self, success: bool = True, error: bool = False, data=[], code: int = 200):
        self.success = success
        self.error = error
        self.data = data or []
        self.code = code if is_status_code(code) else 207

    def get(self):
        return {
                   'code': self.code,
                   'success': self.success,
                   'error': self.error,
                   'data': self.data
               }, self.code


def http_response(func):
    @wraps(func)
    def decorator(*args, **kwargs):
        try:
            data, code = func(*args, **kwargs)
            response = Response(data=data, code=code)
        except UnprocessableEntity as error:
            code = error.code
            args = error.exc.args[0]
            data = [{'field': key, 'error': value[0]} for key, value in args.items()]
            log_error(data)
            response = Response(success=False, error=True, data=data, code=code)
        except DataBaseException as error:
            data = [{'error': error.args[0].orig.args[0]}]
            response = Response(success=False, error=True, data=data, code=422)
        except EntityNotFound as error:
            data = [{'error': error.args[0]}]
            response = Response(success=False, error=True, data=data, code=404)
        except Exception as error:
            log_error(error)
            response = Response(success=False, error=True, code=500)

        return response.get()

    return decorator
