from flask import request
from webargs.flaskparser import parser

from decorators import http_response
from model.config import DBConfig
from model.entities import Usuario
from model.repository import UsuarioRepository
from model.schema import UsuarioSchema
from validations import ADD_USER_ARGS


@http_response
def add_user():
    args = parser.parse(ADD_USER_ARGS, request, location='json')

    config = DBConfig()
    repository = UsuarioRepository(config)
    password = args['password']

    new_user = Usuario(email=args['email'], nome=args['nome'], password=password)
    u = repository.save(new_user)

    schema = UsuarioSchema()
    data = schema.dump(new_user)
    return data, 201
