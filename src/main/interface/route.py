from abc import ABC, abstractmethod
from typing import Type

from src.presenters.helpers import HttpRequest, HttpResponse


class IRoute(ABC):
    @abstractmethod
    def handle(self, http_request: Type[HttpRequest]) -> HttpResponse:
        """Defining Route"""
        raise Exception("Should implement method: route")
