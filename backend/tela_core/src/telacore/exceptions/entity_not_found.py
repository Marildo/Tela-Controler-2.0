from .base_exception import BaseException


class EntityNotFound(BaseException):
    def __init__(self, *args, **kwargs):
        self.status_code = 503

    @property
    def json(self):
        return {
            'description':  self.args[0]
        }
