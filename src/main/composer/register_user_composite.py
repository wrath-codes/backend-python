from src.data.register_user import RegisterUser
from src.infra.repo import UserRepository
from src.main.interface import IRoute
from src.presenters.controllers import RegisterUserController


def register_user_composer() -> IRoute:
    """Composing Register User Route
    :param - None
    :return - IRoute
    """

    repository = UserRepository()
    use_case = RegisterUser(repository)
    register_user_route = RegisterUserController(use_case)

    return register_user_route
