from faker import Faker

from src.infra.test import UserRepositorySpy

from .find import FindUser

fake = Faker()


def test_by_id():
    """Testing by_id method"""
    user_repo = UserRepositorySpy()
    find_user = FindUser(user_repo)

    attributes = {
        "id": fake.random_number(digits=2),
    }
    response = find_user.by_id(id_user=attributes["id"])

    # Testing inputs
    assert user_repo.select_user_params["id_user"] == attributes["id"]

    # Testing outputs
    assert response["Success"] is True
    assert response["Data"]


def test_by_id_fail():
    """Testing by_id fail method"""

    user_repo = UserRepositorySpy()
    find_user = FindUser(user_repo)

    attribute = {"id": fake.word()}
    response = find_user.by_id(id_user=attribute["id"])

    # Testing Input
    assert user_repo.select_user_params == {}

    # Testing Outputs
    assert response["Success"] is False
    assert response["Data"] is None


def test_by_name():
    """Testing by_name method"""
    user_repo = UserRepositorySpy()
    find_user = FindUser(user_repo)

    attributes = {
        "name": fake.name(),
    }
    response = find_user.by_name(name=attributes["name"])

    # Testing inputs
    assert user_repo.select_user_params["name"] == attributes["name"]

    # Testing outputs
    assert response["Success"] is True
    assert response["Data"]


def test_by_name_fail():
    """Testing by_name fail method"""

    user_repo = UserRepositorySpy()
    find_user = FindUser(user_repo)

    attribute = {"name": fake.random_number(digits=2)}
    response = find_user.by_name(name=attribute["name"])

    # Testing Input
    assert user_repo.select_user_params == {}

    # Testing Outputs
    assert response["Success"] is False
    assert response["Data"] is None


def test_by_id_and_name():
    """Testing by_id_and_name method"""
    user_repo = UserRepositorySpy()
    find_user = FindUser(user_repo)

    attributes = {
        "id": fake.random_number(digits=2),
        "name": fake.name(),
    }
    response = find_user.by_id_and_name(
        id_user=attributes["id"], name=attributes["name"]
    )

    # Testing inputs
    assert user_repo.select_user_params["id_user"] == attributes["id"]
    assert user_repo.select_user_params["name"] == attributes["name"]

    # Testing outputs
    assert response["Success"] is True
    assert response["Data"]


def test_by_id_and_name_fail():
    """Testing by_id_and_name fail method"""

    user_repo = UserRepositorySpy()
    find_user = FindUser(user_repo)

    attribute = {"id": fake.word(), "name": fake.random_number(digits=2)}
    response = find_user.by_id_and_name(id_user=attribute["id"], name=attribute["name"])

    # Testing Input
    assert user_repo.select_user_params == {}

    # Testing Outputs
    assert response["Success"] is False
    assert response["Data"] is None
