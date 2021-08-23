from flask import Blueprint
from telacore.decorators import http_response

from app.proxy import RequestProxy
from controller import UnityController
from controller.validations.unity_validations import CREATE_UNITY_ARG

name = 'UnityRouter'
unity_router = Blueprint(name=name, import_name=name, url_prefix='/unidades')


@unity_router.route('', methods=['GET'])
@http_response
def get():
    proxy = RequestProxy()
    controller = UnityController()
    controller.initilize(proxy.validate_credential())
    return controller.read_all()


@unity_router.route('<int:_id>', methods=['GET'])
def get_by_id(_id: int):
    return UnityController().read_by_id(_id)


@unity_router.route('/', methods=['POST'])
@http_response
def post():
    proxy = RequestProxy()
    cred = proxy.validate_credential()
    controller = UnityController()
    args = proxy.validate_args(CREATE_UNITY_ARG)
    controller.initilize(cred)
    return controller.create(args)


@unity_router.route('<int:_id>', methods=['PUT'])
def put(_id: int):
    return UnityController().update(_id)


@unity_router.route('<int:_id>', methods=['DELETE'])
def delete(_id: int):
    return UnityController().delete(_id)
