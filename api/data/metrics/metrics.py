from typing import Any, Dict

from api.data.interfaces import LoggingInterface as Logging
from api.domain.use_cases import Metrics as MetricsInterface


class Metrics(MetricsInterface):
    """Class to define usecase: Scraper"""

    def __init__(self, logging: Logging):
        self.logging = logging

    def generate(self) -> Dict[str, Any]:
        """Generate metrics
        :param - None
        :return - Dictionary with informations of the process
        """

        response = self.logging.generate_metrics()
        return {"Success": True, "Data": response}
