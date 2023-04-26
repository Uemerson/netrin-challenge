from api.domain.use_cases import Metrics
from api.main.interface import RouteInterface
from api.presenters.helpers import HttpRequest, HttpResponse


class MetricsController(RouteInterface):
    """Class to define Route to metrics use case"""

    def __init__(self, metrics_use_case: Metrics):
        self.metrics_use_case = metrics_use_case

    def route(self, http_request: HttpRequest) -> HttpResponse:
        """Method to call use case"""

        response = self.metrics_use_case.generate()
        return HttpResponse(status_code=200, body=response["Data"])
