from .base import Source
import config as cfg

import requests
from datetime import datetime, date
from typing import Optional, Dict
import logging


class CbrSource(Source):

    _ARCHIVE_RATE_TEMPLATE_URL = cfg.CBR_ARCHIVE_TEMPLATE_URL
    _LATEST_RATE_TEMPLATE_URL = cfg.CBR_LATEST_URL
    _DATE_URL_FORMAT = cfg.DATE_FORMAT_CBR

    def _fetch_json(self, url: str) -> Optional[Dict]:
        try:
            r = requests.get(url, timeout=10)
            r.raise_for_status()
            return r.json()
        except requests.RequestException as e:
            logging.error(f"Ошибка запроса к {url}: {e}")
        except ValueError as e:
            logging.error(f"Ошибка парсинга JSON: {e}")
        return None

    def get_rate(self, date_ : date) -> Optional[Dict]:
        cbr_date = date_.strftime(self._DATE_URL_FORMAT)
        url = self._ARCHIVE_RATE_TEMPLATE_URL.format(cbr_date)
        return self._fetch_json(url)

    def get_rate_latest(self) -> Optional[Dict]:
        return self._fetch_json(self._LATEST_RATE_TEMPLATE_URL)




