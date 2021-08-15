from telacore.decorators import http_response

from .auth_controller import valide_token


class UnityController:

    @valide_token
    @http_response
    def read_all(self):
        return {'msg:': 'Popo'}, 200
