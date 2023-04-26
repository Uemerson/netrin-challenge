from abc import ABC, abstractmethod
from typing import Dict, List


class Scraper(ABC):
    """Interface to Scraper use case"""

    @abstractmethod
    def by_q(self, q: str) -> Dict[str, bool | List[str] | None]:
        """Specific case"""

        raise Exception("Should implement method: by_q")
