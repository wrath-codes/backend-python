from faker import Faker

from src.data.test import FindUserSpy
from src.infra.test import UserRepositorySpy
from src.presenters.helpers import HttpRequest

from .find_user_controller import FindUserController

fake = Faker()


def test_handle():
    """Testing handle Method"""

    find_user_use_case = FindUserSpy(UserRepositorySpy())
    find_user_controller = FindUserController(find_user_use_case)

    http_request = HttpRequest(
        query={"user_id": fake.random_number(), "name": fake.word()}
    )

    response = find_user_controller.handle(http_request)

    # Testing Inputs
    assert (
        find_user_use_case.by_id_and_name_params["user_id"]
        == http_request.query["user_id"]
    )
    assert (
        find_user_use_case.by_id_and_name_params["name"] == http_request.query["name"]
    )

    # Testing Outputs
    assert response.status_code == 200
    assert response.body


def test_handle_no_query_params():
    """Testing handle Method with no query params"""

    find_user_use_case = FindUserSpy(UserRepositorySpy())
    find_user_controller = FindUserController(find_user_use_case)

    http_request = HttpRequest()

    response = find_user_controller.handle(http_request)

    # Testing Input
    assert find_user_use_case.by_id_and_name_params == {}
    assert find_user_use_case.by_id_params == {}
    assert find_user_use_case.by_name_params == {}

    # Testing Outputs
    assert response.status_code == 400
    assert "error" in response.body


def test_handle_invalid_query_params():
    """Testing handle Method with invalid query params"""

    find_user_use_case = FindUserSpy(UserRepositorySpy())
    find_user_controller = FindUserController(find_user_use_case)

    http_request = HttpRequest(
        query={"user_id": fake.word(), "name": fake.random_number()}
    )

    response = find_user_controller.handle(http_request)

    # Testing Input
    assert (
        find_user_use_case.by_id_and_name_params["user_id"]
        == http_request.query["user_id"]
    )
    assert (
        find_user_use_case.by_id_and_name_params["name"] == http_request.query["name"]
    )
    assert find_user_use_case.by_id_params == {}
    assert find_user_use_case.by_name_params == {}

    # Testing Outputs
    assert response.status_code == 422
    assert "error" in response.body


def test_handle_no_user_id():
    """Testing handle Method with no user_id query param"""

    find_user_use_case = FindUserSpy(UserRepositorySpy())
    find_user_controller = FindUserController(find_user_use_case)

    http_request = HttpRequest(query={"name": fake.word()})

    response = find_user_controller.handle(http_request)

    # Testing Input
    assert find_user_use_case.by_id_and_name_params == {}
    assert find_user_use_case.by_id_params == {}
    assert find_user_use_case.by_name_params["name"] == http_request.query["name"]

    # Testing Outputs
    assert response.status_code == 200
    assert response.body


def test_handle_no_name():
    """Testing handle Method with no name query param"""

    find_user_use_case = FindUserSpy(UserRepositorySpy())
    find_user_controller = FindUserController(find_user_use_case)

    http_request = HttpRequest(query={"user_id": fake.random_number()})

    response = find_user_controller.handle(http_request)

    # Testing Input
    assert find_user_use_case.by_id_and_name_params == {}
    assert find_user_use_case.by_id_params["user_id"] == http_request.query["user_id"]
    assert find_user_use_case.by_name_params == {}

    # Testing Outputs
    assert response.status_code == 200
    assert response.body


def test_handle_invalid_user_id():
    """Testing handle Method with invalid user_id query param"""

    find_user_use_case = FindUserSpy(UserRepositorySpy())
    find_user_controller = FindUserController(find_user_use_case)

    http_request = HttpRequest(query={"user_id": fake.word()})

    response = find_user_controller.handle(http_request)

    # Testing Input
    assert find_user_use_case.by_id_and_name_params == {}
    assert find_user_use_case.by_id_params["user_id"] == http_request.query["user_id"]
    assert find_user_use_case.by_name_params == {}

    # Testing Outputs
    assert response.status_code == 422
    assert "error" in response.body


def test_handle_invalid_name():
    """Testing handle Method with invalid name query param"""

    find_user_use_case = FindUserSpy(UserRepositorySpy())
    find_user_controller = FindUserController(find_user_use_case)

    http_request = HttpRequest(query={"name": fake.random_number()})

    response = find_user_controller.handle(http_request)

    # Testing Input
    assert find_user_use_case.by_id_and_name_params == {}
    assert find_user_use_case.by_id_params == {}
    assert find_user_use_case.by_name_params["name"] == http_request.query["name"]

    # Testing Outputs
    assert response.status_code == 422
    assert "error" in response.body


def test_handle_wrong_query():
    """Testing handle Method with wrong query param"""

    find_user_use_case = FindUserSpy(UserRepositorySpy())
    find_user_controller = FindUserController(find_user_use_case)

    http_request = HttpRequest(query={"wrong": fake.word()})

    response = find_user_controller.handle(http_request)

    # Testing Input
    assert find_user_use_case.by_id_and_name_params == {}
    assert find_user_use_case.by_id_params == {}
    assert find_user_use_case.by_name_params == {}

    # Testing Outputs
    assert response.status_code == 422
    assert "error" in response.body
