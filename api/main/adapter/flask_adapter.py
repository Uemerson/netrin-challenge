from typing import Any

from api.main.interface import RouteInterface as Route
from api.presenters.errors import HttpErrors
from api.presenters.helpers import HttpRequest, HttpResponse


def flask_adapter(request: Any, api_route: Route) -> Any:
    """Adapter pattern to Flask
    :param - Flask Request
    :api_route: Composite Routes
    """

    try:
        query_string_params = request.args.to_dict()
    except Exception:
        http_error = HttpErrors.error_400()
        return HttpResponse(
            status_code=http_error["status_code"], body=http_error["body"]
        )

    http_request = HttpRequest(
        header=request.headers,
        body=request.get_json(silent=True),
        query=query_string_params,
    )

    try:
        response = api_route.route(http_request)
    except Exception as exc:
        print(exc)
        http_error = HttpErrors.error_500()
        return HttpResponse(
            status_code=http_error["status_code"], body=http_error["body"]
        )

    return response
