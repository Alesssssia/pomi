"""Тест для Этапа 2 — производные классы."""
from media_objects import Image, Video, Audio


def main():
    print("=" * 60)
    print("ТЕСТ 1: Класс Image")
    print("=" * 60)

    img_rgb = Image("photo.jpg", width=1920, height=1080, channels=3)
    print(f"  get_info:        {img_rgb.get_info()}")
    print(f"  get_resolution:  {img_rgb.get_resolution()}")
    print(f"  get_color_space: {img_rgb.get_color_space()}")

    img_gray = Image("scan.png", width=800, height=600, channels=1)
    print(f"\n  Полутоновое:     {img_gray.get_info()}")

    img_rgba = Image("logo.png", width=256, height=256, channels=4)
    print(f"  С альфа-каналом: {img_rgba.get_info()}")

    print("\n" + "=" * 60)
    print("ТЕСТ 2: Класс Video")
    print("=" * 60)

    video = Video("movie.mp4", duration=120, resolution="1920x1080",
                  fps=30, codec="h264")
    print(f"  get_info:   {video.get_info()}")
    print(f"  get_fps:    {video.get_fps()}")
    print(f"  get_codec:  {video.get_codec()}")

    print("\n" + "=" * 60)
    print("ТЕСТ 3: Класс Audio")
    print("=" * 60)

    audio = Audio("music.mp3", duration=180, sample_rate=44100, bitrate=320)
    print(f"  get_info:         {audio.get_info()}")
    print(f"  get_sample_rate:  {audio.get_sample_rate()}")
    print(f"  get_bitrate:      {audio.get_bitrate()}")

    print("\n" + "=" * 60)
    print("ТЕСТ 4: Обработка ошибок")
    print("=" * 60)

    try:
        Image("bad.png", 100, 100, channels=5)
    except ValueError as e:
        print(f"  Поймали: {e}")

    try:
        Video("bad.mp4", 10, "640x480", fps=-1)
    except ValueError as e:
        print(f"  Поймали: {e}")

    try:
        Audio("bad.mp3", 10, sample_rate=0)
    except ValueError as e:
        print(f"  Поймали: {e}")

    print("\n" + "=" * 60)
    print("ТЕСТ 5: Полиморфизм")
    print("=" * 60)

    objects = [
        Image("a.jpg", 1920, 1080, 3),
        Video("b.mp4", 60, "1280x720", 25),
        Audio("c.mp3", 200, 48000, 256),
    ]
    for obj in objects:
        print(f"  {obj.get_info()}")


if __name__ == "__main__":
    main()
