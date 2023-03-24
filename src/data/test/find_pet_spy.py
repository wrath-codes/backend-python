from typing import Dict, List

from src.domain.models import Pets
from src.domain.test import mock_pet


class FindPetSpy:
    """Class to define use case: Select Pet"""

    def __init__(self, pet_repository: any):
        self.pet_repository = pet_repository
        self.by_pet_id_params = {}
        self.by_id_user_params = {}
        self.by_pet_id_and_id_user_params = {}

    def by_pet_id(self, pet_id: int) -> Dict[bool, List[Pets]]:
        """Select Pet by pet_id"""

        self.by_pet_id_params["pet_id"] = pet_id
        response = None
        validate_entry = isinstance(pet_id, int)

        if validate_entry:
            response = [mock_pet()]

        return {"Success": validate_entry, "Data": response}

    def by_user_id(self, id_user: int) -> Dict[bool, List[Pets]]:
        """Select Pet by id_user"""

        self.by_id_user_params["id_user"] = id_user
        response = None
        validate_entry = isinstance(id_user, int)

        if validate_entry:
            response = [mock_pet()]

        return {"Success": validate_entry, "Data": response}

    def by_pet_id_and_user_id(
        self, pet_id: int, id_user: int
    ) -> Dict[bool, List[Pets]]:
        """Select Pet by pet_id and id_user"""

        self.by_pet_id_and_id_user_params["pet_id"] = pet_id
        self.by_pet_id_and_id_user_params["id_user"] = id_user
        response = None
        validate_entry = isinstance(pet_id, int) and isinstance(id_user, int)

        if validate_entry:
            response = [mock_pet()]

        return {"Success": validate_entry, "Data": response}
