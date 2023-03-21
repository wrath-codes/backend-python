from typing import Dict, List, Type

from src.data.interfaces import IPetRepository as PetRepository
from src.domain.models import Pets
from src.domain.use_cases import FindPet as IFindPet


class FindPet(IFindPet):
    """Class to define use case FindPet"""

    def __init__(self, pet_repository: Type[PetRepository]):
        self.pet_repository = pet_repository

    def by_pet_id(self, pet_id: int) -> Dict[bool, List[Pets]]:
        """Select Pet by pet_id
        :param pet_id: id of the pet
        :return: Dict with information about the process
        """

        response = None
        validate_entry = isinstance(pet_id, int)

        if validate_entry:
            response = self.pet_repository.select_pet(pet_id=pet_id)

        return {"Success": validate_entry, "Data": response}

    def by_user_id(self, id_user: int) -> Dict[bool, List[Pets]]:
        """Select Pet by id_user
        :param id_user: id of the user
        :return: Dict with information about the process
        """

        response = None
        validate_entry = isinstance(id_user, int)

        if validate_entry:
            response = self.pet_repository.select_pet(id_user=id_user)

        return {"Success": validate_entry, "Data": response}

    def by_pet_id_and_user_id(
        self, pet_id: int, id_user: int
    ) -> Dict[bool, List[Pets]]:
        """Select Pet by pet_id and id_user
        :param pet_id: id of the pet
        :param id_user: id of the user
        :return: Dict with information about the process
        """

        response = None
        validate_entry = isinstance(pet_id, int) and isinstance(id_user, int)

        if validate_entry:
            response = self.pet_repository.select_pet(pet_id=pet_id, id_user=id_user)

        return {"Success": validate_entry, "Data": response}
