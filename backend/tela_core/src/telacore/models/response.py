from collections import OrderedDict

from flask import make_response, Response
from telacore.exceptions.base_exception import BaseException
from telacore.models.pagination import Pagination
from telacore.utils.logger_util import log_error


class TelaResponse:

    def __init__(self, success: bool = True, data: any = [], code: int = 200, pagination: Pagination = None,
                 error: BaseException = None):
        if error:
            self.success = False
            self.data = error.json
            self.code = error.status_code
        else:
            self.success = success
            self.data = data or []
            self.code = code if self.is_status_code(code) else 207
            self.pagination = pagination

    def get(self) -> Response:
        result = OrderedDict()
        result['code'] = self.code
        result['success'] = self.success
        result['data'] = self.data
        if self.pagination:
            result['pagination'] = self.pagination.json

        resp = make_response(result)
        resp.status_code = self.code
        return resp

    def is_status_code(self, code: int):
        result = code in self.status_code_list()
        if not result:
            log_error(f'{code} is not status code')
        return result

    @staticmethod
    def status_code_list():
        return [100, 101, 102, 200, 201, 202, 203, 204, 205, 206, 207, 208, 226, 300, 301, 302, 303, 304, 305, 307, 308,
                400, 401, 402, 403, 404, 405, 406, 407, 408, 409, 410, 411, 412, 413, 414, 415, 416, 417, 418, 421, 422,
                423, 424, 426, 428, 429, 431, 444, 451, 499, 500, 501, 502, 503, 504, 505, 506, 507, 508, 510, 511, 599]
