from datetime import datetime

from flask import Blueprint
from marshmallow import validate

from .validators.product_validations import PRODUCT_ARGS
from .validators.unity_validations import UPDATE_UNITY_ARGS

name = 'IndexRouter'
index_router = Blueprint(name=name, import_name=name, url_prefix='/')


@index_router.route('', methods=['GET'])
def get():
    return {'Server is running': str(datetime.now())}


@index_router.route('/validations', methods=['GET'])
def validations():
    response = {}

    response.update(load_fiedls('produtos', PRODUCT_ARGS))
    response.update(load_fiedls('unidades', UPDATE_UNITY_ARGS))
    return response


def load_fiedls(name: str, arg):
    fields = {}
    result = ({name: fields})
    for key, values in arg.items():
        propries = {'required': values.required}
        for i in values.validators:
            if isinstance(i, validate.Length):
                propries.update({'length': {'max': i.max, 'min': i.min}})
            elif isinstance(i,validate.Range):
                propries.update({'range': {'max': i.max, 'min': i.min}})


        fields.update({key: propries})


    return result
