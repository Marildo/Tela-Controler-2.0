from .base_exception import BaseException


class DataBaseException(BaseException):
    def __init__(self, *args, **kwargs):
        self.status_code = 503


class DuplicateErrorException(BaseException):
    def __init__(self, *args, **kwargs):
        self.status_code = 422
