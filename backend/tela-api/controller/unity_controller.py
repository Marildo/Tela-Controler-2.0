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
        self.ClassRepository = UnidadeRepository
        self.ClassEntity = Unidade

    @valide_token
    @http_response
    def create(self):
        args = parser.parse(CREATE_UNITY_ARG, request, location='json')
        unity = Unidade(unid=args['unid'], descricao=args['descricao'], fracionavel=args['fracionavel'])
        return self.create_and_dump(unity)

    @valide_token
    @http_response
    def read_all(self):
        return self.read_all_and_dump()

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
