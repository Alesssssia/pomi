from media_objects import MediaObject

# Создаём объект
obj = MediaObject("test.mp4", duration=120)

# Проверяем методы
print(obj.get_info())   # ожидаем: test.mp4: 120 сек
print(obj)              # ожидаем: <MediaObject(test.mp4)>

# Проверяем обработку ошибок
try:
    bad = MediaObject("", duration=10)
except ValueError as e:
    print(f"Поймали ошибку: {e}")

try:
    bad2 = MediaObject("file.mp4", duration=-5)
except ValueError as e:
    print(f"Поймали ошибку: {e}")
