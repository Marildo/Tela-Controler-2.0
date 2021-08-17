from telacore.decorators import http_response

from .auth_controller import valide_token


class UnityController:

    @valide_token
    @http_response
    def read_all(self):
        return {'msg:': 'Read ALL'}, 200

    @valide_token
    @http_response
    def read_by_id(self, _id: int):
        return {'msg:': f'Read By Id {_id}'}, 200

    @valide_token
    @http_response
    def create(self):
        return {'msg:': 'Create'}, 201

    @valide_token
    @http_response
    def update(self, _id: int):
        return {'msg:': f'update {_id}'}, 200

    @valide_token
    @http_response
    def delete(self, _id: int):
        return {'msg:': f'delete {_id}'}, 200
