from abc import ABC, abstractmethod
from typing import Any, Dict


class Metrics(ABC):
    """Interface to Metrics use case"""

    @abstractmethod
    def generate(self) -> Dict[str, Any]:
        """Specific case"""

        raise Exception("Should implement method: generate")
