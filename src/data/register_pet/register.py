from typing import Dict, List, Type

from src.data.find_user import FindUser
from src.data.interfaces import IPetRepository as PetRepository
from src.domain.models import Pets, Users
from src.domain.use_cases import RegisterPet as IRegisterPet


class RegisterPet(IRegisterPet):
    """Class to define use case: Register Pet"""

    def __init__(self, pet_repository: Type[PetRepository], find_user: Type[FindUser]):
        self.pet_repository = pet_repository
        self.find_user = find_user

    def registry(
        self, name: str, specie: str, user_information: Dict[int, str], age: int = None
    ) -> Dict[bool, Pets]:
        """Registry Pet
        :param - name: pet name
                   - specie: type of the specie
                   - age: age of the pet
                   - user_information: Dictionary with id_user and/or user_name
        :return - Dictionary with information about the process
        """

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
            response = self.pet_repository.insert_pet(
                name, specie, age, user_information["id_user"]
            )

        return {"Success": checker, "Data": response}

    def __find_user_information(
        self, user_information: Dict[int, str]
    ) -> Dict[bool, List[Users]]:
        """Check user Infos and select user
        :param - user_information: Dictionary with id_user and/or user_name
        :return - Dictionary with the response of find_user use case"""

        user_found = None
        user_params = user_information.keys()

        if "id_user" in user_params and "user_name" in user_params:
            user_found = self.find_user.by_id_and_name(
                user_information["id_user"], user_information["user_name"]
            )

        elif "id_user" not in user_params and "user_name" in user_params:
            user_found = self.find_user.by_name(user_information["user_name"])

        elif "id_user" in user_params and "user_name" not in user_params:
            user_found = self.find_user.by_id(user_information["id_user"])

        else:
            return {"Success": False, "Data": None}

        return user_found
