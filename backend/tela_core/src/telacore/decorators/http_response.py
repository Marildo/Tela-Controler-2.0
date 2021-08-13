from functools import wraps

from werkzeug.exceptions import UnprocessableEntity

from telacore.models.response import Response
from telacore.exceptions import EntityNotFound, DataBaseException
from telacore.utils.logger_util import log_error


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
            response = Response(success=False, data=data, code=code)
        except DataBaseException as error:
            data = {'error': error.args[0].orig.args[0]}
            response = Response(success=False, data=data, code=422)
        except EntityNotFound as error:
            data = {'error': error.args[0]}
            response = Response(success=False, data=data, code=404)
        except Exception as error:
            log_error(error)
            data = {'error': error.args[0]}
            response = Response(success=False, data=data, code=500)

        return response.get()

    return decorator
