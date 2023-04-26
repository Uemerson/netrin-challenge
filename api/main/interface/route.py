from abc import ABC, abstractmethod

from api.presenters.helpers import HttpRequest, HttpResponse


class RouteInterface(ABC):
    """Interface to Routes"""

    @abstractmethod
    def route(self, http_request: HttpRequest) -> HttpResponse:
        """Defining Route"""

        raise Exception("Should implement method: route")
