from hashlib import sha512


class SecurityUtil:

    @staticmethod
    def hash(value: str) -> str:
        return sha512(value.encode('utf-8')).hexdigest()
