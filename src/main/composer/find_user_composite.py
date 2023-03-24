from src.data.find_user import FindUser
from src.infra.repo import UserRepository
from src.presenters.controllers import FindUserController


def find_user_composer() -> FindUserController:
    """Composing Find User Controller
    :param - None
    :return - Object with Find User Route
    """
    repository = UserRepository()
    use_case = FindUser(repository)
    find_user_route = FindUserController(use_case)

    return find_user_route
