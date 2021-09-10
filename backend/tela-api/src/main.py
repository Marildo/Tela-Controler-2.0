try:
    import sys
    import os
    current_dir = os.path.dirname(__file__)
    source_path = os.path.abspath(os.path.join(current_dir, '../'))
    sys.path.append(source_path)
except:
    raise


from app import TelaAPP
from settings import Settings

if __name__ == '__main__':
    settings = Settings()
    app = TelaAPP().app
    app.run(debug=settings.get_debug(), port=settings.get_api_port())
