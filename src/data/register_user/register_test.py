from faker import Faker

from src.infra.test import UserRepositorySpy

from .register import RegisterUser

fake = Faker()


def test_register():
    """Testing registry method"""

    user_repo = UserRepositorySpy()
    register_user = RegisterUser(user_repo)

    atributes = {
        "name": fake.name(),
        "password": fake.name(),
    }

    response = register_user.register(
        name=atributes["name"], password=atributes["password"]
    )

    # Testing input
    assert user_repo.insert_user_params["name"] == atributes["name"]
    assert user_repo.insert_user_params["password"] == atributes["password"]

    # Testing outputs
    assert response["Success"] is True
    assert response["Data"]


def test_register_fail():
    """Testing registry method"""

    user_repo = UserRepositorySpy()
    register_user = RegisterUser(user_repo)

    atributes = {
        "name": fake.random_number(digits=2),  # Invalid name
        "password": fake.name(),
    }

    response = register_user.register(
        name=atributes["name"], password=atributes["password"]
    )

    # Testing input
    assert user_repo.insert_user_params == {}

    # Testing outputs
    assert response["Success"] is False
    assert response["Data"] is None
