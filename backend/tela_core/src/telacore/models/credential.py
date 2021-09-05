class Credential:
    def __init__(self, cnpj: str, user_id: int, permissoes) -> None:
        self.cnpj = cnpj
        self.id = user_id
        self.permissoes = permissoes
