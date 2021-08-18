from flask import request
from telacore.decorators import http_response
from webargs.flaskparser import parser

from controller import BaseController
from controller.schemas import UnitySchema
from controller.validations.unity_validations import CREATE_UNITY_ARG
from model.entities import Unidade
from model.repository import UnidadeRepository
from .auth_controller import valide_token


class UnityController(BaseController):

    def __init__(self) -> None:
        super().__init__()
        self.schema = UnitySchema()

    @valide_token
    @http_response
    def create(self):
        args = parser.parse(CREATE_UNITY_ARG, request, location='json')
        unity = Unidade(unid=args['unid'], descricao=args['descricao'], fracionavel=args['fracionavel'])
        repository = UnidadeRepository(self.cnpj)
        repository.save(unity)
        data = self.schema.dump(unity)

        return data, 201

    @valide_token
    @http_response
    def read_all(self):
        repository = UnidadeRepository(self.cnpj)
        unitys = repository.find_all(Unidade)
        data = self.schema.dump(unitys, many=True)
        return data, 200

    @valide_token
    @http_response
    def read_by_id(self, _id: int):
        return {'msg:': f'Read By Id {_id}'}, 200

    @valide_token
    @http_response
    def update(self, _id: int):
        return {'msg:': f'update {_id}'}, 200

    @valide_token
    @http_response
    def delete(self, _id: int):
        return {'msg:': f'delete {_id}'}, 200
