from flask import Flask
from flask_cors import CORS
from flask_restful import Api

from settings import Settings
from routes import AppRouter

app = Flask('Tela-API')
CORS(app, resources={r"*": {"origins": "*"}})
api = Api(app)

router = AppRouter(api)
router.load()

if __name__ == '__main__':
    settings = Settings()
    app.run(debug=settings.get_debug(), port=settings.get_api_port())
