from faker import Faker

from src.data.test import FindPetSpy
from src.infra.test import PetRepositorySpy
from src.presenters.controllers import FindPetController
from src.presenters.helpers import HttpRequest

fake = Faker()


def test_handle():
    """Testing handle Method"""

    find_pet_use_case = FindPetSpy(PetRepositorySpy())
    find_pet_controller = FindPetController(find_pet_use_case)

    http_request = HttpRequest(
        query={"pet_id": fake.random_number(), "id_user": fake.random_number()}
    )

    response = find_pet_controller.handle(http_request)

    # Testing Inputs
    assert (
        find_pet_use_case.by_pet_id_and_id_user_params["pet_id"]
        == http_request.query["pet_id"]
    )
    assert (
        find_pet_use_case.by_pet_id_and_id_user_params["id_user"]
        == http_request.query["id_user"]
    )

    # Testing Outputs
    assert response.status_code == 200
    assert response.body


def test_handle_no_query_params():
    """Testing handle Method with no query params"""

    find_pet_use_case = FindPetSpy(PetRepositorySpy())
    find_pet_controller = FindPetController(find_pet_use_case)

    http_request = HttpRequest()

    response = find_pet_controller.handle(http_request)

    # Testing Input
    assert find_pet_use_case.by_pet_id_and_id_user_params == {}
    assert find_pet_use_case.by_pet_id_params == {}
    assert find_pet_use_case.by_id_user_params == {}

    # Testing Outputs
    assert response.status_code == 400
    assert "error" in response.body


def test_handle_invalid_query_params():
    """Testing handle Method with invalid query params"""

    find_pet_use_case = FindPetSpy(PetRepositorySpy())
    find_pet_controller = FindPetController(find_pet_use_case)

    http_request = HttpRequest(query={"pet_id": fake.word(), "id_user": fake.word()})

    response = find_pet_controller.handle(http_request)

    # Testing Input
    assert (
        find_pet_use_case.by_pet_id_and_id_user_params["pet_id"]
        == http_request.query["pet_id"]
    )
    assert (
        find_pet_use_case.by_pet_id_and_id_user_params["id_user"]
        == http_request.query["id_user"]
    )
    assert find_pet_use_case.by_pet_id_params == {}
    assert find_pet_use_case.by_id_user_params == {}

    # Testing Outputs
    assert response.status_code == 422
    assert "error" in response.body


def test_handle_no_pet_id():
    """Testing handle Method with no pet_id"""

    find_pet_use_case = FindPetSpy(PetRepositorySpy())
    find_pet_controller = FindPetController(find_pet_use_case)

    http_request = HttpRequest(query={"id_user": fake.random_number()})

    response = find_pet_controller.handle(http_request)

    # Testing Input
    assert find_pet_use_case.by_pet_id_and_id_user_params == {}
    assert find_pet_use_case.by_pet_id_params == {}
    assert (
        find_pet_use_case.by_id_user_params["id_user"] == http_request.query["id_user"]
    )

    # Testing Outputs
    assert response.status_code == 200
    assert response.body


def test_handle_no_id_user():
    """Testing handle Method with no id_user"""

    find_pet_use_case = FindPetSpy(PetRepositorySpy())
    find_pet_controller = FindPetController(find_pet_use_case)

    http_request = HttpRequest(query={"pet_id": fake.random_number()})

    response = find_pet_controller.handle(http_request)

    # Testing Input
    assert find_pet_use_case.by_pet_id_and_id_user_params == {}
    assert find_pet_use_case.by_pet_id_params["pet_id"] == http_request.query["pet_id"]
    assert find_pet_use_case.by_id_user_params == {}

    # Testing Outputs
    assert response.status_code == 200
    assert response.body


def test_handle_invalid_pet_id():
    """Testing handle Method with invalid pet_id"""

    find_pet_use_case = FindPetSpy(PetRepositorySpy())
    find_pet_controller = FindPetController(find_pet_use_case)

    http_request = HttpRequest(query={"pet_id": fake.word()})

    response = find_pet_controller.handle(http_request)

    # Testing Input
    assert find_pet_use_case.by_pet_id_and_id_user_params == {}
    assert find_pet_use_case.by_pet_id_params["pet_id"] == http_request.query["pet_id"]
    assert find_pet_use_case.by_id_user_params == {}

    # Testing Outputs
    assert response.status_code == 422
    assert "error" in response.body


def test_handle_invalid_id_user():
    """Testing handle Method with invalid id_user"""

    find_pet_use_case = FindPetSpy(PetRepositorySpy())
    find_pet_controller = FindPetController(find_pet_use_case)

    http_request = HttpRequest(query={"id_user": fake.word()})

    response = find_pet_controller.handle(http_request)

    # Testing Input
    assert find_pet_use_case.by_pet_id_and_id_user_params == {}
    assert find_pet_use_case.by_pet_id_params == {}
    assert (
        find_pet_use_case.by_id_user_params["id_user"] == http_request.query["id_user"]
    )

    # Testing Outputs
    assert response.status_code == 422
    assert "error" in response.body


def test_handle_wrong_query():
    """Testing handle Method with wrong query"""

    find_pet_use_case = FindPetSpy(PetRepositorySpy())
    find_pet_controller = FindPetController(find_pet_use_case)

    http_request = HttpRequest(query={"wrong": fake.word()})

    response = find_pet_controller.handle(http_request)

    # Testing Input
    assert find_pet_use_case.by_pet_id_and_id_user_params == {}
    assert find_pet_use_case.by_pet_id_params == {}
    assert find_pet_use_case.by_id_user_params == {}

    # Testing Outputs
    assert response.status_code == 422
    assert "error" in response.body
