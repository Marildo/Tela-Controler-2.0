from typing import Dict
import math

class Pagination:
    def __init__(self, total: int, page: int, size: int, ) -> None:
        self.total = total
        self.page = page
        self.size = size

    @property
    def json(self) -> Dict:
        return {
            'total': self.total,
            'page': self.page,
            'size': self.size,
            'total_pages': math.ceil(self.total / self.size)
        }
