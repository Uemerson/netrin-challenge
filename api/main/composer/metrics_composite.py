from api.data.metrics import Metrics
from api.infra.utils.logging import Logging
from api.presenters.controllers import MetricsController


def metrics_composer() -> MetricsController:
    """Composing Metrics Route
    :param - None
    :return - Object with Metrics Route
    """

    logging = Logging()
    use_case = Metrics(logging)
    metrics_route = MetricsController(use_case)

    return metrics_route
