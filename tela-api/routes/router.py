from flask_restful import Api

from .index_router import IndexRouter


class AppRouter:
    def __init__(self, api: Api):
        self.__api: Api = api

    def load(self):
        api = self.__api
        api.add_resource(IndexRouter, '/')
