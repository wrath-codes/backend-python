from typing import Dict, List

from src.domain.models import Pets, Users
from src.domain.test import mock_pet, mock_users


class RegisterPetSpy:
    """Class to define use case: Register Pet"""

    def __init__(self, pet_repository: any, find_user: any):
        self.pet_repository = pet_repository
        self.find_user = find_user
        self.registry_params = {}

    def registry(
        self, name: str, specie: str, user_information: Dict[int, str], age: int = None
    ) -> Dict[bool, Pets]:
        """Registry Pet"""

        self.registry_params = {
            "name": name,
            "specie": specie,
            "user_information": user_information,
            "age": age,
        }

        response = None

        # Validating entry and trying to find an user
        validate_entry = (
            isinstance(name, str)
            and isinstance(specie, str)
            and (age is None or isinstance(age, int))
        )
        user = self.__find_user_information(user_information)
        checker = validate_entry and user["Success"]

        if checker:
            response = mock_pet()

        return {"Success": checker, "Data": response}

    @classmethod
    def __find_user_information(
        cls, user_information: Dict[int, str]
    ) -> Dict[bool, List[Users]]:
        """Check userInfo Dictionary and select user"""

        user_found = None
        user_params = user_information.keys()

        if "user_id" and "name" in user_params:
            # find user by id and name
            user_found = {"Success": True, "Data": mock_users()}

        elif "name" not in user_params and "user_id" in user_params:
            # find user by id
            user_found = {"Success": True, "Data": mock_users()}

        elif "user_id" not in user_params and "name" in user_params:
            # find user by name
            user_found = {"Success": True, "Data": mock_users()}

        else:
            return {"Success": False, "Data": None}

        return user_found
