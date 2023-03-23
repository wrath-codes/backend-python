from typing import Type

from src.domain.use_cases import FindPet
from src.presenters.errors import HttpErrors
from src.presenters.helpers import HttpRequest, HttpResponse


class FindPetController:
    """Class to define controller to find_pet use case"""

    def __init__(self, find_pet_use_case: Type[FindPet]):
        self.find_pet_use_case = find_pet_use_case

    def handle(self, http_request: Type[HttpRequest]) -> HttpResponse:
        """Methods to call use case"""

        response = None

        if http_request.query:
            # if query

            query_string_params = http_request.query.keys()

            if "pet_id" in query_string_params and "id_user" in query_string_params:
                pet_id = http_request.query["pet_id"]
                id_user = http_request.query["id_user"]
                response = self.find_pet_use_case.by_pet_id_and_id_user(
                    pet_id=pet_id, id_user=id_user
                )

            elif (
                "pet_id" in query_string_params and "id_user" not in query_string_params
            ):
                pet_id = http_request.query["pet_id"]
                response = self.find_pet_use_case.by_pet_id(pet_id=pet_id)

            elif (
                "pet_id" not in query_string_params and "id_user" in query_string_params
            ):
                id_user = http_request.query["id_user"]
                response = self.find_pet_use_case.by_id_user(id_user=id_user)

            else:
                response = {"Success": False, "Data": None}

            if response["Success"] is False:
                http_error = HttpErrors.error_422()
                return HttpResponse(
                    status_code=http_error["status_code"],
                    body=http_error["body"],
                )

            return HttpResponse(status_code=200, body=response["Data"])

        # if no query in http_request
        http_error = HttpErrors.error_400()
        return HttpResponse(
            status_code=http_error["status_code"],
            body=http_error["body"],
        )
