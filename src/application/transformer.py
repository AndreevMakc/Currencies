from src.models.valutes import Valute
from datetime import datetime

def transform_json_from_cbr(data):
    target_currency_json = {}
    for currency in data:
        date_ = datetime.fromisoformat(currency['Date']).strftime('%Y-%m-%d')
        valute_data = {}
        for code, val in currency['Valute'].items():
            if code in Valute.__members__:
                valute_data[code] = val['Value']
        target_currency_json[date_] = valute_data
    return target_currency_json
