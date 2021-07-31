from flask import Flask
from flask_cors import CORS
from flask_restful import Api

from settings import config_logger
from routes import AppRouter

config_logger()

app = Flask('Tela-API')
CORS(app, resources={r"*": {"origins": "*"}})
api = Api(app)

router = AppRouter(api)
router.load()

if __name__ == '__main__':
    app.run(debug=True, port=9000)
