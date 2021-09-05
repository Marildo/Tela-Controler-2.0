from .base_exception import BaseException

class UnauthorizationException(BaseException):
    def __init__(self,status_code, *args, **kwargs):
        self.status_code = status_code

    @property
    def json(self):
        value = self.args
        return {
            'error': {
                'description': value[1]
            }
        }
