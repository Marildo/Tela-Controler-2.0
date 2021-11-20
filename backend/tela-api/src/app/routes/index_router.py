from datetime import datetime

from flask import Blueprint, request
from marshmallow import validate,fields

from .validators.product_validations import PRODUCT_ARGS
from .validators.section_validations import SECTION_ARGS
from .validators.unity_validations import UNITY_ARGS

name = 'IndexRouter'
index_router = Blueprint(name=name, import_name=name, url_prefix='/')


@index_router.route('', methods=['GET'])
def get():
    return {'Server is running': str(datetime.now())}


@index_router.route('/validations', methods=['GET','PUT'])
def validations():
    headers = request.headers

    response = {}
    response.update(load_fiedls('produtos', PRODUCT_ARGS))
    response.update(load_fiedls('setores', SECTION_ARGS))
    response.update(load_fiedls('unidades', UNITY_ARGS))
    return response


def load_fiedls(name: str, arg):
    _fields = {}
    result = ({name: _fields})
    for key, values in arg.items():
        propries = {'required': values.required}
        if isinstance(values, fields.Nested):
            v = load_fiedls('fields', values.schema.fields)
            propries.update(v['fields'])
        else:
            if values.missing:
                propries['default'] = values.missing

            for i in values.validators:
                if isinstance(i, validate.Length):
                    propries.update({'length': {'max': i.max, 'min': i.min}})
                elif isinstance(i, validate.Range):
                    propries.update({'range': {'max': i.max, 'min': i.min}})

        _fields.update({key: propries})

    return result
