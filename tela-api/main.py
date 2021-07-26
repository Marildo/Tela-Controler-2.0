from flask import Flask
from flask_restful import Api
from routes import AppRouter

app = Flask(__name__)
api = Api(app)

router = AppRouter(api)
router.load()

if __name__ == '__main__':
    app.run(debug=True, port=9000)
