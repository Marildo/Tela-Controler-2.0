from .db_iconnection import IDBConnection


class MysqlConnection(IDBConnection):

    def _get_url(self) -> str:
        settings = self._config
        user = settings.user
        password = settings.password
        port = settings.port
        host = settings.host
        database = settings.database
        charset = settings.get_database_charset()
        return f'mysql+pymysql://{user}:{password}@{host}:{port}/{database}?charset={charset}'
        return url
