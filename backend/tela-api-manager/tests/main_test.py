from telacore.exceptions import DataBaseException
from telacore.decorators import http_response

@http_response
def test():
    raise DataBaseException('dsdsdds')


test()