from typing import Dict, List

from src.domain.models import Users
from src.domain.test import mock_users


class FindUserSpy:
    """Class to define usecase: Select User"""

    def __init__(self, user_repository: any):
        self.user_repository = user_repository
        self.by_id_params = {}
        self.by_name_params = {}
        self.by_id_and_name_params = {}

    def by_id(self, id_user: int) -> Dict[bool, List[Users]]:
        """Select User by id"""

        self.by_id_params["id_user"] = id_user
        response = None
        validate_entry = isinstance(id_user, int)

        if validate_entry:
            response = [mock_users()]

        return {"Success": validate_entry, "Data": response}

    def by_name(self, name: str) -> Dict[bool, List[Users]]:
        """Select User by name"""

        self.by_name_params["name"] = name
        response = None
        validate_entry = isinstance(name, str)

        if validate_entry:
            response = [mock_users()]

        return {"Success": validate_entry, "Data": response}

    def by_id_and_name(self, id_user: int, name: str) -> Dict[bool, List[Users]]:
        """Select User by id and name"""

        self.by_id_and_name_params["id_user"] = id_user
        self.by_id_and_name_params["name"] = name
        response = None
        validate_entry = isinstance(id_user, int) and isinstance(name, str)

        if validate_entry:
            response = [mock_users()]

        return {"Success": validate_entry, "Data": response}
