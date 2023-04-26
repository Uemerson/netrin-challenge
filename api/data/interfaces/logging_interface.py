from abc import ABC, abstractmethod


class LoggingInterface(ABC):
    """Interface to Logging"""

    @abstractmethod
    def log(self, time: float, q: str) -> None:
        """abstractmethod"""

        raise Exception("Method not implemented")
