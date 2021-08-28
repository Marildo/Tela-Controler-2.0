class DataBaseException(Exception):
    pass


class DuplicateErrorException(Exception):
    def json(self):
        value = self.args[0].orig.args
        return {
            'code': value[0],
            'description': value[1]
        }
