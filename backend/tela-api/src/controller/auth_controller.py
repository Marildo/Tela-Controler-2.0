from typing import Dict

from flask import request
from telacore.exceptions import EntityNotFound
from telacore.utils import CNPJUtil, SecurityUtil
from telacore.utils.logger_util import log_error
from webargs.flaskparser import parser

from src.app.routes.validators import LOGIN_ARGS
from src.controller.schemas import UsuarioSchema
from src.model.entities import Usuario
from src.model.repository import UsuarioRepository
from src.services import AuthService


def login():
    try:
        args = parser.parse(LOGIN_ARGS, request, location='json')
        cnpj = CNPJUtil.decode(args['codigo'])
        user = find_for_login(cnpj=cnpj, email=args['email'], password=args['password'])
        token = AuthService().encode(cnpj=cnpj, payload=user)
        return {'token': token}, 200
    except Exception as error:
        log_error(error)
        data = 'Dados inválidos'
        return data, 401


def create_user_and_login(cnpj, args) -> str:
    email = args['email']
    nome = args['nome']
    password = SecurityUtil.hash(args['password'])

    user = Usuario(email=email, nome=nome, password=password)
    repository = UsuarioRepository(cnpj)
    repository.save(user)
    data = find_for_login(cnpj=cnpj, email=user.email, password=args['password'])
    token = AuthService().encode(cnpj, data)
    return token


def find_for_login(cnpj, email, password) -> Dict:
    repository = UsuarioRepository(cnpj)
    user = repository.find_by_email(email)
    if user and user.password == SecurityUtil.hash(password):
        data = UsuarioSchema().dump(user)
        permissions = repository.load_permissions(user.id)
        data.update({'permissoes': permissions})
        return data
    raise EntityNotFound('Senha ou email incorretos')
