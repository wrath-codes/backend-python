from faker import Faker

from src.data.test import RegisterPetSpy
from src.infra.test import PetRepositorySpy, UserRepositorySpy
from src.presenters.helpers import HttpRequest

from .register_pet_controller import RegisterPetController

fake = Faker()


def test_handle():
    """Testing handle method in RegisterPetController"""

    register_pet_use_case = RegisterPetSpy(PetRepositorySpy(), UserRepositorySpy())
    register_pet_route = RegisterPetController(register_pet_use_case)

    attributes = {
        "name": fake.word(),
        "specie": "dog",
        "age": fake.random_number(),
        "user_information": {
            "user_id": fake.random_number(),
            "name": fake.name(),
        },
    }

    response = register_pet_route.handle(HttpRequest(body=attributes))

    # Testing Inputs
    assert register_pet_use_case.registry_params["name"] == attributes["name"]
    assert register_pet_use_case.registry_params["specie"] == attributes["specie"]
    assert register_pet_use_case.registry_params["age"] == attributes["age"]
    assert (
        register_pet_use_case.registry_params["user_information"]
        == attributes["user_information"]
    )

    # Testing Outputs
    assert response.status_code == 200
    assert "error" not in response.body


def test_handle_no_age():
    """Testing route method in RegisterPetController"""

    register_pet_use_case = RegisterPetSpy(PetRepositorySpy(), UserRepositorySpy())
    register_pet_route = RegisterPetController(register_pet_use_case)

    attributes = {
        "name": fake.word(),
        "specie": "dog",
        "user_information": {
            "user_id": fake.random_number(),
            "name": fake.name(),
        },
    }

    response = register_pet_route.handle(HttpRequest(body=attributes))

    # Testing Inputs
    assert register_pet_use_case.registry_params["name"] == attributes["name"]
    assert register_pet_use_case.registry_params["specie"] == attributes["specie"]
    assert register_pet_use_case.registry_params["age"] is None
    assert (
        register_pet_use_case.registry_params["user_information"]
        == attributes["user_information"]
    )

    # Testing Outputs
    assert response.status_code == 200
    assert "error" not in response.body


def test_handle_no_user_id():
    """Testing route method in RegisterPetController"""

    register_pet_use_case = RegisterPetSpy(PetRepositorySpy(), UserRepositorySpy())
    register_pet_route = RegisterPetController(register_pet_use_case)

    attributes = {
        "name": fake.word(),
        "specie": "dog",
        "age": fake.random_number(),
        "user_information": {
            "name": fake.name(),
        },
    }

    response = register_pet_route.handle(HttpRequest(body=attributes))

    # Testing Inputs
    assert register_pet_use_case.registry_params["name"] == attributes["name"]
    assert register_pet_use_case.registry_params["specie"] == attributes["specie"]
    assert register_pet_use_case.registry_params["age"] == attributes["age"]
    assert (
        register_pet_use_case.registry_params["user_information"]
        == attributes["user_information"]
    )

    # Testing Outputs
    assert response.status_code == 200
    assert "error" not in response.body


def test_handle_no_user_name():
    """Testing route method in RegisterPetController"""

    register_pet_use_case = RegisterPetSpy(PetRepositorySpy(), UserRepositorySpy())
    register_pet_route = RegisterPetController(register_pet_use_case)

    attributes = {
        "name": fake.word(),
        "specie": "dog",
        "age": fake.random_number(),
        "user_information": {
            "id_user": fake.random_number(),
        },
    }

    response = register_pet_route.handle(HttpRequest(body=attributes))

    # Testing Inputs
    assert register_pet_use_case.registry_params["name"] == attributes["name"]
    assert register_pet_use_case.registry_params["specie"] == attributes["specie"]
    assert register_pet_use_case.registry_params["age"] == attributes["age"]
    assert (
        register_pet_use_case.registry_params["user_information"]
        == attributes["user_information"]
    )

    # Testing Outputs
    assert response.status_code == 422
    assert "error" in response.body


def test_handle_error_wrong_user_information():
    """Testing route method in RegisterUserRouter"""

    register_pet_use_case = RegisterPetSpy(PetRepositorySpy(), UserRepositorySpy())
    register_pet_route = RegisterPetController(register_pet_use_case)

    attributes = {"name": fake.word(), "specie": "dog", "user_information": {}}

    response = register_pet_route.handle(HttpRequest(body=attributes))

    # Testing input
    assert register_pet_use_case.registry_params == {}

    # Testing output
    assert response.status_code == 422
    assert "error" in response.body


def test_handle_no_body():
    """Testing route method in RegisterUserRouter"""

    register_pet_use_case = RegisterPetSpy(PetRepositorySpy(), UserRepositorySpy())
    register_pet_route = RegisterPetController(register_pet_use_case)

    response = register_pet_route.handle(HttpRequest())

    # Testing input
    assert register_pet_use_case.registry_params == {}

    # Testing output
    assert response.status_code == 400
    assert "error" in response.body


def test_handle_wrong_body():
    """Testing route method in RegisterUserRouter"""

    register_pet_use_case = RegisterPetSpy(PetRepositorySpy(), UserRepositorySpy())
    register_pet_route = RegisterPetController(register_pet_use_case)

    attributes = {
        "specie": "dog",
        "user_information": {
            "user_id": fake.random_number(),
            "name": fake.name(),
        },
    }

    response = register_pet_route.handle(HttpRequest(body=attributes))

    # Testing input
    assert register_pet_use_case.registry_params == {}

    # Testing output
    assert response.status_code == 422
    assert "error" in response.body
