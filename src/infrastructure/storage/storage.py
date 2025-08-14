import logging
from abc import ABC, abstractmethod
import json
import os
from typing import Optional

from .storage_exceptions import FileNotFound, FileEmpty

class Storage(ABC):

    @abstractmethod
    def read_json(self):
        pass

    @abstractmethod
    def write_json(self, data):
        pass


class FileHandler(Storage):
    def __init__(self, file):
        super().__init__()
        self.file = file

    def read_json(self) -> Optional[json]:
        try:
            if not os.path.exists(self.file):
                raise FileNotFound(self.file)
            if not os.path.getsize(self.file) > 0:
                raise FileEmpty(self.file)
            with open(self.file, 'r', encoding='utf-8') as file_:
                return json.load(file_)
        except FileNotFound as e:
            logging.error(e)
        except FileEmpty as e:
            logging.error(e)
        return None

    def write_json(self, data):
        with open(self.file, "w", encoding='utf-8') as file_:
            json.dump(data, file_, ensure_ascii=False, indent=4)





