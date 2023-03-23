from typing import Dict

from src.domain.models import Users
from src.domain.test import mock_users


class RegisterUserSpy:
    """Class to define use case: Register User"""

    def __init__(self, user_repository: any):
        self.user_repository = user_repository
        self.register_params = {}

    def register(self, name: str, password: str) -> Dict[bool, Users]:
        """Registry User"""

        self.register_params = {"name": name, "password": password}

        response = None

        # Validating entry
        validate_entry = isinstance(name, str) and isinstance(password, str)

        if validate_entry:
            response = mock_users()

        return {"Success": validate_entry, "Data": response}
