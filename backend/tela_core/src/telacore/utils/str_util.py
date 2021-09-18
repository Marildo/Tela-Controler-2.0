from unicodedata import normalize


class StrUtil:

    @staticmethod
    def normalize(text: str) -> str:
        return normalize('NFKD', text).encode('ASCII', 'ignore').decode('ASCII')
