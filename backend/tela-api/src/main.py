from app import TelaAPP
from settings import Settings

if __name__ == '__main__':
    settings = Settings()
    app = TelaAPP().app
    app.run(debug=settings.get_debug(), port=settings.get_api_port())
