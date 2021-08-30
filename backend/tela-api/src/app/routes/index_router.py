from datetime import datetime

from flask import Blueprint

name = 'IndexRouter'
index_router = Blueprint(name=name, import_name=name, url_prefix='/')


@index_router.route('', methods=['GET'])
def get():
    return {'Server is running': str(datetime.now())}
