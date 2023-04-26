import time
from typing import Dict, List

from api.data.interfaces import GoogleScraperInterface as GoogleScraper
from api.data.interfaces import LoggingInterface as Logging
from api.domain.use_cases import Scraper as ScraperInterface


class Scraper(ScraperInterface):
    """Class to define usecase: Scraper"""

    def __init__(self, google_scraper: GoogleScraper, logging: Logging):
        self.google_scraper = google_scraper
        self.logging = logging

    def by_q(self, q: str) -> Dict[str, bool | List[str] | None]:
        """Scraper Links By q
        :param - q: string of the query
        :return - Dictionary with informations of the process
        """

        response = None
        validate_entry = isinstance(q, str)

        if validate_entry:
            start_time = time.time()
            response = self.google_scraper.scraper(q=q)
            self.logging.log(time=(time.time() - start_time), q=q)

        return {"Success": validate_entry, "Data": response}
