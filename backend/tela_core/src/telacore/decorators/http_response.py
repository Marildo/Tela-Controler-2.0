from functools import wraps

from werkzeug.exceptions import UnprocessableEntity

from telacore.exceptions import EntityNotFound, DataBaseException, DuplicateErrorException, UnauthorizationException
from telacore.models.response import TelaResponse
from telacore.utils.logger_util import log_error


# TODO - Traduzir mensagem de erros
# TODO - Retornar erro sempre dentro de um array

def http_response(func):
    @wraps(func)
    def decorator(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            data, code = result[0:2]
            pagination = result[2] if len(result) == 3 else None
            response = TelaResponse(data=data, code=code, pagination=pagination)
        except UnprocessableEntity as error:
            code = error.code
            args = error.exc.args[0]

            data = []
            for key, value in args.items():
                if isinstance(value, dict):
                    if '_schema' in value:
                        value = value['_schema']

                data.append({'field': key, 'error': value[0]})

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
