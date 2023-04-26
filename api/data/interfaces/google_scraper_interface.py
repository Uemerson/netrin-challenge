from abc import ABC, abstractmethod
from typing import List


class GoogleScraperInterface(ABC):
    """Interface to Google Scraper"""

    @abstractmethod
    def scraper(self, q: str) -> List[str]:
        """abstractmethod"""

        raise Exception("Method not implemented")
