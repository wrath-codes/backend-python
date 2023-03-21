from faker import Faker

from src.data.test import FindUserSpy
from src.infra.test import PetRepositorySpy, UserRepositorySpy

from .register import RegisterPet

fake = Faker()


def test_registry():
    """Testing Registry method in RegisterPet use case"""

    pet_repo = PetRepositorySpy()
    find_user = FindUserSpy(UserRepositorySpy())
    register_pet = RegisterPet(pet_repo, find_user)

    attributes = {
        "name": fake.name(),
        "specie": fake.name(),
        "age": fake.random_number(digits=1),
        "user_information": {
            "user_id": fake.random_number(digits=5),
            "user_name": fake.name(),
        },
    }

    response = register_pet.registry(
        name=attributes["name"],
        specie=attributes["specie"],
        age=attributes["age"],
        user_information=attributes["user_information"],
    )

    # Testing inputs
    assert pet_repo.insert_pet_params["name"] == attributes["name"]
    assert pet_repo.insert_pet_params["specie"] == attributes["specie"]
    assert pet_repo.insert_pet_params["age"] == attributes["age"]

    # Testing FindUser Inputs
    assert (
        find_user.by_id_and_name_params["user_id"]
        == attributes["user_information"]["user_id"]
    )
    assert (
        find_user.by_id_and_name_params["name"]
        == attributes["user_information"]["user_name"]
    )

    # Testing Outputs
    assert response["Success"] is True
    assert response["Data"]
