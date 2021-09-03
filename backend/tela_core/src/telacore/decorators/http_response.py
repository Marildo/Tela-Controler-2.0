from functools import wraps

from flask import Response
from telacore.exceptions import EntityNotFound, DataBaseException, DuplicateErrorException, UnauthorizationException
from telacore.models.response import TelaResponse
from telacore.utils.logger_util import log_error
from werkzeug.exceptions import UnprocessableEntity


# TODO - Traduzir mensagem de erros

def http_response(func) -> Response:
    @wraps(func)
    def decorator(*args, **kwargs):
        try:
            data, code = func(*args, **kwargs)
            response = TelaResponse(data=data, code=code)
        except UnprocessableEntity as error:
            code = error.code
            args = error.exc.args[0]
            data = [{'field': key, 'error': value[0]} for key, value in args.items()]
            log_error(data)
            response = TelaResponse(success=False, data=data, code=code)
        except (DuplicateErrorException, DataBaseException, EntityNotFound) as error:
            response = TelaResponse(error=error)
        except UnauthorizationException as error:
            data = {'error': str(error.args[0])}
            response = TelaResponse(success=False, data=data, code=401)
        except Exception as error:
            log_error(error)
            data = {'error': error.args[0]}
            response = TelaResponse(success=False, data=data, code=500)

        return response.get()

    return decorator
