from brutils import cnpj


class CNPJUtil:

    @staticmethod
    def validate(_cnpj):
        return cnpj.validate(_cnpj)

    @staticmethod
    def mask(_cnpj):
        return cnpj.display(str(_cnpj))
