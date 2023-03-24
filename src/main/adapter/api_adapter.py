from typing import Type

from sqlalchemy.exc import IntegrityError

from src.main.interface import IRoute as Route
from src.presenters.errors import HttpErrors
from src.presenters.helpers import HttpRequest, HttpResponse


def flask_adapter(request: any, api_route: Type[Route]) -> any:
    """Adapter pattern to Flask
    :param - Flask Request
    :api_route: Composite Routes
    """

    try:
        # Query string params
        query_string_params = request.args.to_dict()

        # Formatting information
        if "id_user" in query_string_params.keys():
            query_string_params["id_user"] = int(query_string_params["id_user"])

        if "pet_id" in query_string_params.keys():
            query_string_params["pet_id"] = int(query_string_params["pet_id"])
    except:
        https_error = HttpErrors.error_400()
        return HttpResponse(
            status_code=https_error["status_code"], body=https_error["body"]
        )

    http_request = HttpRequest(
        header=request.headers, body=request, query=query_string_params
    )

    try:
        response = api_route.handle(http_request)

    except IntegrityError:
        https_error = HttpErrors.error_409()
        return HttpResponse(
            status_code=https_error["status_code"], body=https_error["body"]
        )
    except:
        https_error = HttpErrors.error_500()
        return HttpResponse(
            status_code=https_error["status_code"], body=https_error["body"]
        )
    return response
