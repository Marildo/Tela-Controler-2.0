from telacore.utils.logger_util import log_error


class Response:

    def __init__(self, success: bool = True, data=[], code: int = 200):
        self.success = success
        self.data = data or []
        self.code = code if self.is_status_code(code) else 207

    def get(self):
        return {
                   'code': self.code,
                   'success': self.success,
                   'data': self.data
               }, self.code

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
