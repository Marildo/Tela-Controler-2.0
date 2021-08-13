from enum import Enum, IntEnum
from typing import List


class Perfil(Enum):
    A = 'A'
    B = 'C'
    C = 'C'

    @staticmethod
    def keys(cls) -> List:
        return [i.key for i in cls]

    @staticmethod
    def value(cls):
        return [i.value for i in cls]
