from flask import Flask
from flask_restful import Api
from flask_cors import CORS

from settings import config_logger

config_logger()

app = Flask(__name__)
cors = CORS(app, resources={r"*": {"origins": "*"}})
api = Api(app)

from routes import AppRouter

router = AppRouter(api)
router.load()

if __name__ == '__main__':
    app.run(debug=True, port=9000)
