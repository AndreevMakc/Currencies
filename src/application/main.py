from datetime import date
from src.infrastructure.clients.cbr import CbrSource
from fetcher import DataFetcher
from src.infrastructure.storage.storage import FileHandler
from transformer import transform_json_from_cbr

def migration():
    data_fetcher = DataFetcher(CbrSource())
    data = (transform_json_from_cbr(
        data_fetcher.get_rates_by_period(date(2022, 1, 1), date(2025, 8, 13))))
    file = FileHandler('currency.json')
    file.write_json(data)


def main():
    migration()

if __name__ == '__main__':
    main()