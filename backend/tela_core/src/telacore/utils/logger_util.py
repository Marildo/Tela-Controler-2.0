import logging

from flask import request


def log_error(msg):
    error = {
        'msg': msg,
        'path': request.path,
        'method': request.method,
        'data': request.data
    }
    logging.error(error)
