from datetime import datetime

from flask_restful import Resource


class IndexRouter(Resource):
    def get(self):
        return {'Server is running': str(datetime.now())}
