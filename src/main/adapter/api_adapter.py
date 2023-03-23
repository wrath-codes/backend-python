from typing import Type

from sqlalchemy.exc import IntegrityError

from src.main.interface import IRoute as Route
from src.presenters.errors import HttpErrors
from src.presenters.helpers import HttpRequest, HttpResponse


def flask_adapter(request: any, api_route: Type[Route]) -> any:
    """Adapter pattern for Flask
    :param - request: Flask Request
           - api_route: Composite Routes
    """

    http_request = HttpRequest(
        body=request.json,
    )
    try:
        response = api_route.handle(http_request)
    except IntegrityError:
        http_error = HttpErrors.error_409()
        return HttpResponse(
            status_code=http_error["status_code"],
            body=http_error["body"],
        )

    return response
