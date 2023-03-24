from typing import Dict, List, Type

from src.data.interfaces import IUserRepository as UserRepository
from src.domain.models import Users
from src.domain.use_cases import FindUser as IFindUser


class FindUser(IFindUser):
    """Class to define use case FindUser"""

    def __init__(self, user_repository: Type[UserRepository]):
        self.user_repository = user_repository

    def by_id(self, id_user: int) -> Dict[bool, List[Users]]:
        """Select User by id
        :param id_user: id of the user
        :return: Dict with information about the process
        """

        response = None
        validate_entry = isinstance(id_user, int)

        if validate_entry:
            response = self.user_repository.select_user(id_user=id_user)

        return {"Success": validate_entry, "Data": response}

    def by_name(self, name: str) -> Dict[bool, List[Users]]:
        """Select User by name
        :param name: name of the user
        :return: Dict with information about the process
        """

        response = None
        validate_entry = isinstance(name, str)

        if validate_entry:
            response = self.user_repository.select_user(name=name)

        return {"Success": validate_entry, "Data": response}

    def by_id_and_name(self, id_user: int, name: str) -> Dict[bool, List[Users]]:
        """Select User by id and name
        :param id_user: id of the user
        :param name: name of the user
        :return: Dict with information about the process
        """

        response = None
        validate_entry = isinstance(id_user, int) and isinstance(name, str)

        if validate_entry:
            response = self.user_repository.select_user(id_user=id_user, name=name)

        return {"Success": validate_entry, "Data": response}
