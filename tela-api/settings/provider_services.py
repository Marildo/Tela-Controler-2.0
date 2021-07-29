from services import IAuth, JWTService


class ProviderServices:
    def __init__(self):
        self.__authService = JWTService()

    def auth_service(self) -> IAuth:
        return self.__authService


provider_services = ProviderServices()
