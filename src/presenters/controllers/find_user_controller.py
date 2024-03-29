from typing import Type

from src.domain.use_cases import FindUser
from src.main.interface import IRoute
from src.presenters.errors import HttpErrors
from src.presenters.helpers import HttpRequest, HttpResponse


class FindUserController(IRoute):
    """Class to define controller to find_user use case"""

    def __init__(self, find_user_use_case: Type[FindUser]):
        self.find_user_use_case = find_user_use_case

    def handle(self, http_request: Type[HttpRequest]) -> HttpResponse:
        """Method to call use case"""

        response = None

        if http_request.query:
            # if query

            query_string_params = http_request.query.keys()

            if "id_user" in query_string_params and "name" in query_string_params:
                id_user = http_request.query["id_user"]
                name = http_request.query["name"]
                response = self.find_user_use_case.by_id_and_name(
                    id_user=id_user, name=name
                )

            elif "id_user" in query_string_params and "name" not in query_string_params:
                id_user = http_request.query["id_user"]
                response = self.find_user_use_case.by_id(id_user=id_user)

            elif "id_user" not in query_string_params and "name" in query_string_params:
                name = http_request.query["name"]
                response = self.find_user_use_case.by_name(name=name)

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
