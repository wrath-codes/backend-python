from typing import List

from src.domain.models import Users
from src.domain.test import mock_users


class UserRepositorySpy:
    """Spy for User Repository"""

    def __init__(self):
        self.insert_user_params = {}
        self.select_user_params = {}

    def insert_user(self, name: str, password: str) -> Users:
        """Spy to all the attributes of the method"""

        self.insert_user_params["name"] = name
        self.insert_user_params["password"] = password

        return mock_users()

    def select_user(self, id_user: int = None, name: str = None) -> List[Users]:
        """Spy to all the attributes of the method"""

        self.select_user_params["id_user"] = id_user
        self.select_user_params["name"] = name

        return [mock_users()]
