class QueryPage:
    def __init__(self, page: int, size: int, orderby: str, sort: str) -> None:
        self.page = int(page) if page and int(page) > 0 else 1
        self.size = int(size) if size and int(size) > 0 else 50
        self.orderby = orderby
        self._sort = sort

    @property
    def offset(self):
        return (self.page - 1) * self.size

    @property
    def sort(self) -> str:
        if self._sort == 'desc':
            return self._sort

        return 'asc'
