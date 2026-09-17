"""

Модуль с фильтрами изображений.

Вариант 1: Изображения (JPEG, PNG).
Используется абстрактный класс ImageFilter и три конкретных фильтра.
"""
from abc import ABC, abstractmethod

import cv2
import numpy as np


class ImageFilter(ABC):
    """Абстрактный базовый класс для фильтров изображений.

    Наследники обязаны реализовать метод apply().
    """

    @abstractmethod
    def apply(self, image_data):
        """Применяет фильтр к изображению (numpy-массив) и возвращает результат."""
        pass

    def __str__(self):
        return f"<{self.__class__.__name__}>"


class BrightnessFilter(ImageFilter):
    """Фильтр изменения яркости.

    factor > 1 — ярче, factor < 1 — темнее.
    """

    def __init__(self, factor: float = 1.5):
        if factor <= 0:
            raise ValueError("Коэффициент яркости должен быть положительным")
        self.factor = factor

    def apply(self, image_data):
        """Умножает пиксели на коэффициент (с ограничением 0..255)."""
        result = cv2.convertScaleAbs(image_data, alpha=self.factor, beta=0)
        return result


class ContrastFilter(ImageFilter):
    """Фильтр изменения контраста.

    factor > 1 — контрастнее, factor < 1 — мягче.
    """

    def __init__(self, factor: float = 1.5):
        if factor <= 0:
            raise ValueError("Коэффициент контраста должен быть положительным")
        self.factor = factor

    def apply(self, image_data):
        """Формула: (pixel - 128) * factor + 128, с ограничением 0..255."""
        mean = 128.0
        result = (image_data.astype(np.float32) - mean) * self.factor + mean
        return np.clip(result, 0, 255).astype(np.uint8)


class BlurFilter(ImageFilter):
    """Фильтр размытия (Gaussian Blur).

    kernel_size — размер ядра (нечётное число, например 3, 5, 7).
    """

    def __init__(self, kernel_size: int = 5):
        if kernel_size < 3 or kernel_size % 2 == 0:
            raise ValueError("kernel_size должен быть нечётным и >= 3")
        self.kernel_size = kernel_size

    def apply(self, image_data):
        """Применяет гауссово размытие."""
        result = cv2.GaussianBlur(
            image_data,
            (self.kernel_size, self.kernel_size),
            0
        )
        return result


def process_image(image_data, filters):
    """Применяет последовательность фильтров к изображению.

    Демонстрирует полиморфизм: filters — список объектов ImageFilter.
    """
    result = image_data
    for filter_obj in filters:
        result = filter_obj.apply(result)
    return result
