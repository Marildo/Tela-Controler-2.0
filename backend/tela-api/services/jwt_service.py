import logging
from datetime import datetime, timedelta
from typing import Dict

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
import jwt

from services import IAuth


class JWTService(IAuth):

    def __init__(self):
        logging.info('Carregando JWT Service')
        self.__file_key = "C:/Users/Cesar/developer/Tela-Controler-2.0/helpers/tela.pem"
        self.__algorithm = 'RS256'
        self.__expiration = datetime.now() + timedelta(minutes=60 * 24)

    def encode(self, payload: Dict) -> str:
        jwt_token = jwt.encode({'exp': self.__expiration, 'payload': payload},
                           key=self.__load_private_key(),
                           algorithm=self.__algorithm)
        return jwt_token

    def decode(self, token):
        private_key = self.__load_private_key()
        payload = jwt.decode(token, private_key.public_key(), algorithms=self.__algorithm)
        return payload

    def __load_private_key(self):
        with open(self.__file_key, "rb") as key_file:
            private_key = serialization.load_pem_private_key(
                key_file.read(),
                password=None,
                backend=default_backend()
            )
        return private_key
