class QueryPage:
    def __init__(self, page: int, size: int, orderby: str, sort: str) -> None:
        self.page = page
        self.size = size
        self.orderby = orderby
        self._sort = sort

    @property
    def sort(self) -> str:
        if self._sort == 'desc':
            return self._sort

        return 'asc'
