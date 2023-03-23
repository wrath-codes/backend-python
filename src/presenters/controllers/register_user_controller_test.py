from faker import Faker

from src.data.test import RegisterUserSpy
from src.infra.test import UserRepositorySpy
from src.presenters.helpers import HttpRequest

from .register_user_controller import RegisterUserController

fake = Faker()


def test_handle():
    """Testing handle method in RegisterUserController"""

    register_user_use_case = RegisterUserSpy(UserRepositorySpy())
    register_user_route = RegisterUserController(register_user_use_case)

    attributes = {
        "name": fake.word(),
        "password": fake.word(),
    }

    response = register_user_route.handle(HttpRequest(body=attributes))

    # Testing Inputs
    assert register_user_use_case.register_params["name"] == attributes["name"]
    assert register_user_use_case.register_params["password"] == attributes["password"]

    # Testing Outputs
    assert response.status_code == 200
    assert "error" not in response.body


def test_handle_no_body():
    """Testing handle method in RegisterUserController"""

    register_user_use_case = RegisterUserSpy(UserRepositorySpy())
    register_user_route = RegisterUserController(register_user_use_case)

    response = register_user_route.handle(HttpRequest())

    # Testing Outputs
    assert response.status_code == 400
    assert "error" in response.body


def test_handle_wrong_body():
    """Testing handle method in RegisterUserController"""

    register_user_use_case = RegisterUserSpy(UserRepositorySpy())
    register_user_route = RegisterUserController(register_user_use_case)

    attributes = {
        "name": fake.word(),
    }

    response = register_user_route.handle(HttpRequest(body=attributes))

    # Testing Outputs
    assert response.status_code == 422
    assert "error" in response.body
