class BaseStorageException(Exception):
    pass


class FileNotFound(BaseStorageException):
    def __init__(self, file):
        message = f"Файл {file} не найден"
        super().__init__(message)
        self.file = file

class FileEmpty(BaseStorageException):
    def __init__(self, file):
        message = f"Файл {file} пустой"
        super().__init__(message)
        self.file = file