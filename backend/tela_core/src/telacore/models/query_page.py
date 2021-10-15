from typing import Dict, Tuple


class QueryPage:
    def __init__(self, args: Dict) -> None:
        self._args = args
        self._page = int(args['page']) if 'page' in args else 1
        self.size = int(args['size']) if 'size' in args else 50
        self.field_name = args['fieldname'] if 'fieldname' in args else None

    @property
    def offset(self) -> int:
        return (self.page - 1) * self.size

    @property
    def page(self) -> int:
        return self._page if self._page > 0 else 1

    def orderby(self) -> Tuple[str, str]:
        if 'orderby' in self._args:
            order = self._args['orderby'].split(':')
            sort = order[-1]
            sort = sort if sort == 'desc' else 'asc'
            return order[0], sort

    def field_like(self) -> bool:
        self.field_value = self._args['like'] if 'like' in self._args else None
        return self.field_value != None

