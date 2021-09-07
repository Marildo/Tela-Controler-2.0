from .db_iconnection import IDBConnection


class MysqlConnection(IDBConnection):

    def _get_url(self) -> str:
        settings = self._config
        user = settings.user
        password = settings.password
        port = settings.port
        host = settings.host
        database = settings.database if settings.database != 'emp_None' else 'mysql'
        charset = settings.charset
        return f'mysql+pymysql://{user}:{password}@{host}:{port}/{database}?charset={charset}'
