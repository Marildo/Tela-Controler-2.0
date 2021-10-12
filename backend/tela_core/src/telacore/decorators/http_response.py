from functools import wraps

from flask import Response
from telacore.exceptions import EntityNotFound, DataBaseException, DuplicateErrorException, UnauthorizationException
from telacore.models.response import TelaResponse
from telacore.utils.logger_util import log_error
from werkzeug.exceptions import UnprocessableEntity


# TODO - Traduzir mensagem de erros
# TODO - Retornar erro sempre dentro de um array

def http_response(func) -> Response:
    @wraps(func)
    def decorator(*args, **kwargs):
        try:
            data, code, pagination = func(*args, **kwargs)
            response = TelaResponse(data=data, code=code, pagination=pagination)
        except UnprocessableEntity as error:
            code = error.code
            args = error.exc.args[0]
            data = [{'field': key, 'error': value[0]} for key, value in args.items()]
            log_error(data)
            response = TelaResponse(success=False, data=data, code=code)
        except (DuplicateErrorException, DataBaseException, EntityNotFound,
                UnauthorizationException) as error:
            response = TelaResponse(error=error)
        except Exception as error:
            log_error(error)
            data = {'error': error.args[0]}
            response = TelaResponse(success=False, data=data, code=500)

        return response.get()

    return decorator
