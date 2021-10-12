from typing import Dict
import math

class Pagination:
    def __init__(self, total: int, page: str, size: int, ) -> None:
        self.total = int(total)
        self.page = int(page)
        self.size = int(size)

    @property
    def json(self) -> Dict:
        return {
            'total': self.total,
            'page': self.page,
            'size': self.size,
            'total_pages': math.ceil(self.total / self.size)
        }
