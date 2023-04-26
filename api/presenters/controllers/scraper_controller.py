from api.domain.use_cases import Scraper
from api.main.interface import RouteInterface
from api.presenters.errors import HttpErrors
from api.presenters.helpers import HttpRequest, HttpResponse


class ScraperController(RouteInterface):
    """Class to define Route to scraper use case"""

    def __init__(self, scraper_use_case: Scraper):
        self.scraper_use_case = scraper_use_case

    def route(self, http_request: HttpRequest) -> HttpResponse:
        """Method to call use case"""

        response = None

        if http_request.query:
            query_string_params = http_request.query.keys()

            if "q" in query_string_params:
                q = http_request.query["q"]
                response = self.scraper_use_case.by_q(q=q)
            else:
                response = {"Success": False, "Data": None}

            if response["Success"] is False:
                https_error = HttpErrors.error_422()
                return HttpResponse(
                    status_code=https_error["status_code"], body=https_error["body"]
                )

            return HttpResponse(status_code=200, body=response["Data"])

        https_error = HttpErrors.error_400()
        return HttpResponse(
            status_code=https_error["status_code"], body=https_error["body"]
        )
