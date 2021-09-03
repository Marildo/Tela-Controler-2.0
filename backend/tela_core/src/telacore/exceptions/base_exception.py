class BaseException(Exception):
    def __init__(self, *args, **kwargs):
        super.__init__(*args, **kwargs)
        self.status_code = 503

    @property
    def json(self):
        value = self.args[0].orig.args
        return {
            'error': {
                'code': value[0],
                'description': value[1]
            }
        }
