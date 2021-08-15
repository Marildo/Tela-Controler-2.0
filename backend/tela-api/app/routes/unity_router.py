from flask import Blueprint

from controller import UnityController

name = 'UnityRouter'
unity_router = Blueprint(name=name, import_name=name, url_prefix='/unidades')


@unity_router.route('/', methods=['GET'])
def get():
    return UnityController().read_all()
