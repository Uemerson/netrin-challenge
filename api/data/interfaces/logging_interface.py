from abc import ABC, abstractmethod
from typing import Any, Dict


class LoggingInterface(ABC):
    """Interface to Logging"""

    @abstractmethod
    def log(self, time: float, q: str) -> None:
        """abstractmethod"""

        raise Exception("Method not implemented")

    @abstractmethod
    def generate_metrics(self) -> Dict[str, Any]:
        """abstractmethod"""

        raise Exception("Method not implemented")
