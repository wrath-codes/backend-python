from faker import Faker

from src.infra.test import PetRepositorySpy

from .find import FindPet

fake = Faker()


def test_by_pet_id():
    """Testing by_pet_id in FindPet"""

    pet_repo = PetRepositorySpy()
    find_pet = FindPet(pet_repo)

    attribute = {"pet_id": fake.random_number(digits=5)}
    response = find_pet.by_pet_id(pet_id=attribute["pet_id"])

    # Testing Input
    assert pet_repo.select_pet_params["pet_id"] == attribute["pet_id"]

    # Testing Outputs
    assert response["Success"] is True
    assert response["Data"]


def test_by_pet_id_fail():
    """Testing by_pet_id fail in FindPet"""

    pet_repo = PetRepositorySpy()
    find_pet = FindPet(pet_repo)

    attribute = {"pet_id": fake.word()}
    response = find_pet.by_pet_id(pet_id=attribute["pet_id"])

    # Testing Inputs
    assert pet_repo.select_pet_params == {}

    # Testing Outputs
    assert response["Success"] is False
    assert response["Data"] is None


def test_by_user_id():
    """Testing by_user_id in FindPet"""

    pet_repo = PetRepositorySpy()
    find_pet = FindPet(pet_repo)

    attributes = {"id_user": fake.random_number(digits=5)}
    response = find_pet.by_user_id(id_user=attributes["id_user"])

    # Testing Inputs
    assert pet_repo.select_pet_params["id_user"] == attributes["id_user"]

    # Testing Outputs
    assert response["Success"] is True
    assert response["Data"]


def test_by_user_id_fail():
    """Testing by_user_id fail in FindPet"""

    pet_repo = PetRepositorySpy()
    find_pet = FindPet(pet_repo)

    attributes = {"id_user": fake.word()}
    response = find_pet.by_user_id(id_user=attributes["id_user"])

    # Testing Inputs
    assert pet_repo.select_pet_params == {}

    # Testing Outputs
    assert response["Success"] is False
    assert response["Data"] is None


def test_by_pet_id_and_user_id():
    """Testing by_pet_id_and_user_id in FindPet"""

    pet_repo = PetRepositorySpy()
    find_pet = FindPet(pet_repo)

    attributes = {
        "pet_id": fake.random_number(digits=5),
        "id_user": fake.random_number(digits=5),
    }
    response = find_pet.by_pet_id_and_user_id(
        pet_id=attributes["pet_id"], id_user=attributes["id_user"]
    )

    # Testing Inputs
    assert pet_repo.select_pet_params["pet_id"] == attributes["pet_id"]
    assert pet_repo.select_pet_params["id_user"] == attributes["id_user"]

    # Testing Outputs
    assert response["Success"] is True
    assert response["Data"]


def test_by_pet_id_and_user_id_fail():
    """Testing by_pet_id_and_user_id fail in FindPet"""

    pet_repo = PetRepositorySpy()
    find_pet = FindPet(pet_repo)

    attributes = {
        "pet_id": fake.word(),
        "id_user": fake.word(),
    }
    response = find_pet.by_pet_id_and_user_id(
        pet_id=attributes["pet_id"], id_user=attributes["id_user"]
    )

    # Testing Inputs
    assert pet_repo.select_pet_params == {}

    # Testing Outputs
    assert response["Success"] is False
    assert response["Data"] is None
