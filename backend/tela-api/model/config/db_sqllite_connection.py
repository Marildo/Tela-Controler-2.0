from .db_iconnection import IDBConnection


class SqlLiteConnection(IDBConnection):

    def _get_url(self) -> str:
        url = f'sqlite:///{self._config.database}.db'
        return url
