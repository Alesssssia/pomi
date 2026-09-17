"""
Модуль с классами для мультимедийных объектов.
Вариант 1: Изображения (JPEG, PNG).
"""


class MediaObject:
    """Базовый класс для всех мультимедийных объектов.

    Атрибуты:
        filename (str): имя файла
        duration (float): длительность в секундах (для изображений = 0)
    """

    def __init__(self, filename, duration=0):
        # Проверка корректности имени файла
        if not filename or not isinstance(filename, str):
            raise ValueError("Имя файла не может быть пустым")
        # Проверка длительности
        if duration < 0:
            raise ValueError("Длительность не может быть отрицательной")

        self.filename = filename
        self.duration = duration

    def get_info(self):
        """Возвращает строку с информацией об объекте."""
        return f"{self.filename}: {self.duration} сек"

    def __str__(self):
        """Строковое представление — используется в print()."""
        return f"<{self.__class__.__name__}({self.filename})>"
