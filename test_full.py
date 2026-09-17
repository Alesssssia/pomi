"""Финальный тест ЛР1 — проверка всех классов и фильтров."""
import os

import cv2
import numpy as np

from media_objects import MediaObject, Image, Video, Audio, MediaLibrary
from filters import BrightnessFilter, ContrastFilter, BlurFilter, process_image


def section(title):
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)


def main():
    # ---------- 1. Создание объектов ----------
    section("1. Создание медиаобъектов")

    img = Image("photo.jpg", width=1920, height=1080, channels=3)
    img_gray = Image("scan.png", width=800, height=600, channels=1)
    video = Video("movie.mp4", duration=120, resolution="1920x1080",
                  fps=30, codec="h264")
    audio = Audio("music.mp3", duration=180, sample_rate=44100, bitrate=320)

    print(f"  {img.get_info()}")
    print(f"  {img_gray.get_info()}")
    print(f"  {video.get_info()}")
    print(f"  {audio.get_info()}")

    # ---------- 2. MediaLibrary ----------
    section("2. MediaLibrary: добавление и статистика")

    lib = MediaLibrary()
    lib.add(img)
    lib.add(img_gray)
    lib.add(video)
    lib.add(audio)

    print(f"  Всего объектов:      {len(lib)}")
    print(f"  Общая длительность:  {lib.get_total_duration()} сек")
    print(f"  Изображений:         {len(lib.filter_by_type(Image))}")
    print(f"  Видео:               {len(lib.filter_by_type(Video))}")
    print(f"  Аудио:               {len(lib.filter_by_type(Audio))}")

    # ---------- 3. Фильтры на синтетическом изображении ----------
    section("3. Фильтры изображений")

    # Создаём синтетическое изображение 200x200 с градиентом
    test_img = np.zeros((200, 200, 3), dtype=np.uint8)
    for i in range(200):
        test_img[i, :] = i  # градиент по вертикали

    print(f"  Исходное:  shape={test_img.shape}, "
          f"mean={test_img.mean():.1f}, min={test_img.min()}, max={test_img.max()}")

    # 3.1 Яркость
    bright = BrightnessFilter(1.5)
    res_bright = bright.apply(test_img)
    print(f"  Яркость 1.5:   mean={res_bright.mean():.1f}, "
          f"max={res_bright.max()}")

    # 3.2 Контраст
    contrast = ContrastFilter(1.8)
    res_contrast = contrast.apply(test_img)
    print(f"  Контраст 1.8:  mean={res_contrast.mean():.1f}, "
          f"std={res_contrast.std():.1f}")

    # 3.3 Размытие
    blur = BlurFilter(7)
    res_blur = blur.apply(test_img)
    print(f"  Размытие 7:    shape={res_blur.shape}, "
          f"mean={res_blur.mean():.1f}")

    # ---------- 4. Полиморфизм: последовательность фильтров ----------
    section("4. Полиморфизм: цепочка фильтров")

    filters = [
        BrightnessFilter(1.2),
        ContrastFilter(1.3),
        BlurFilter(5),
    ]
    result = process_image(test_img, filters)
    print(f"  Цепочка {filters}")
    print(f"  Результат: shape={result.shape}, mean={result.mean():.1f}")

    # ---------- 5. Применение к реальному файлу (если есть) ----------
    section("5. Работа с реальным файлом (если есть)")

    real_path = "sample.jpg"
    if os.path.exists(real_path):
        real = cv2.imread(real_path)
        if real is not None:
            print(f"  Загружено: {real_path}, shape={real.shape}")
            out = process_image(real, [BrightnessFilter(1.3), BlurFilter(3)])
            cv2.imwrite("sample_out.jpg", out)
            print(f"  Сохранено: sample_out.jpg")
        else:
            print(f"  Не удалось прочитать {real_path}")
    else:
        print(f"  Файл {real_path} не найден — пропускаем")
        print(f"  (Положи любой jpg рядом с test_full.py и перезапусти)")

    # ---------- 6. Обработка ошибок ----------
    section("6. Обработка ошибок")

    try:
        Image("bad.png", 100, 100, channels=7)
    except ValueError as e:
        print(f"  Ошибка каналов:   {e}")

    try:
        Video("bad.mp4", -5, "640x480")
    except ValueError as e:
        print(f"  Ошибка duration:  {e}")

    try:
        lib.add("не медиаобъект")
    except TypeError as e:
        print(f"  Ошибка add:       {e}")

    try:
        BlurFilter(4)  # чётное число
    except ValueError as e:
        print(f"  Ошибка blur:      {e}")

    section("ТЕСТ ЗАВЕРШЁН")


if __name__ == "__main__":
    main()
