from datetime import date, timedelta
from src.infrastructure.clients.cbr import Source
from typing import Optional, List

class DataFetcher:

    def __init__(self, source: Source):
        self.source = source

    def get_rates_by_period(self, date_from_at: date, date_to_at: date) -> Optional[List]:
        current_time = date_from_at
        all_rates = []
        while current_time <= date_to_at:
            rate = self.source.get_rate(current_time)
            if rate:
                all_rates.append(rate)
            current_time += timedelta(days=1)
        return all_rates


