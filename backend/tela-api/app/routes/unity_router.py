from flask import Blueprint

from controller import UnityController

name = 'UnityRouter'
unity_router = Blueprint(name=name, import_name=name, url_prefix='/unidades')


@unity_router.route('', methods=['GET'])
def get():
    return UnityController().read_all()


@unity_router.route('<int:_id>', methods=['GET'])
def get_by_id(_id: int):
    return UnityController().read_by_id(_id)


@unity_router.route('/', methods=['POST'])
def post():
    return UnityController().create()


@unity_router.route('<int:_id>', methods=['PUT'])
def put(_id: int):
    return UnityController().update(_id)


@unity_router.route('<int:_id>', methods=['DELETE'])
def delete(_id: int):
    return UnityController().delete(_id)
