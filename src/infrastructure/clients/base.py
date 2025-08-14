from abc import ABC, abstractmethod
from datetime import date

class Source(ABC):

    @abstractmethod
    def get_rate(self, date_: date):
        pass

    @abstractmethod
    def get_rate_latest(self):
        pass