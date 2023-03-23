from typing import Dict, Type

from src.data.interfaces import IUserRepository as UserRepository
from src.domain.models import Users
from src.domain.use_cases import RegisterUser as IRegisterUser


class RegisterUser(IRegisterUser):
    """Class to define use case : Register User"""

    def __init__(self, user_repository: Type[UserRepository]):
        self.user_repository = user_repository

    def register(self, name: str, password: str) -> Dict[bool, Users]:
        """Register User use case
        :param - name: person name
               - password: person password
        :return - Dict[bool, Optional[Users]]
        """

        response = None
        validate_entry = isinstance(name, str) and isinstance(password, str)

        if validate_entry:
            response = self.user_repository.insert_user(name, password)

        return {"Success": validate_entry, "Data": response}
