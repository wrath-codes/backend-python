from typing import List

from src.domain.models import Pets
from src.domain.test import mock_pet


class PetRepositorySpy:
    """Spy to Pet Repository"""

    def __init__(self):
        self.insert_pet_params = {}
        self.select_pet_params = {}

    def insert_pet(self, name: str, specie: str, age: int, id_user: int) -> Pets:
        """Spy all the attributes"""

        self.insert_pet_params["name"] = name
        self.insert_pet_params["specie"] = specie
        self.insert_pet_params["age"] = age
        self.insert_pet_params["id_user"] = id_user

        return mock_pet()

    def select_pet(self, pet_id: int = None, id_user: int = None) -> List[Pets]:
        """Spy all the attributes"""

        self.select_pet_params["pet_id"] = pet_id
        self.select_pet_params["id_user"] = id_user

        return [mock_pet()]
