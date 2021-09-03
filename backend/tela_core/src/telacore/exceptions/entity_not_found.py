from .base_exception import BaseException


class EntityNotFound(BaseException):
    def __init__(self):
        self.status_code = 503

    def json(self):
        value = self.args[0]
        return {
            'description': value[0]
        }
