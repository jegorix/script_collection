import cv2
from typing import Tuple


'''
📄 Описание
Скрипт автоматически находит лица на изображении с помощью алгоритма Хаара, размывает их (блюрит) и сохраняет новое изображение на диск.

📦 Зависимости
- opencv-python
- typing (входит в стандартную библиотеку)

Установка OpenCV:
pip install opencv-python

🧠 Функции

load_image(path: str) -> cv2.Mat
Загружает изображение с указанного пути.
📌 Бросает FileNotFoundError, если файл не найден.

detect_faces(image: cv2.Mat) -> Tuple[Tuple[int, int, int, int], ...]
Находит лица на изображении, используя каскад Хаара.
📌 Возвращает кортеж координат прямоугольников (x, y, w, h) для каждого лица.

blur_faces(image: cv2.Mat, faces: Tuple[Tuple[int, int, int, int], ...]) -> cv2.Mat
Размывает каждое найденное лицо на изображении с помощью GaussianBlur.

save_image(image: cv2.Mat, path: str) -> None
Сохраняет изображение на диск по указанному пути.

🚀 Запуск
Измени путь к изображению в переменной input_path и запусти скрипт:
python script.py

'''




def load_image(path: str) -> cv2.Mat:
    """Загружает изображение с указанного пути."""
    image = cv2.imread(path)
    if image is None:
        raise FileNotFoundError(f"Изображение не найдено: {path}")
    return image


def detect_faces(image: cv2.Mat) -> Tuple[Tuple[int, int, int, int], ...]:
    """Находит лица на изображении с помощью каскада Хаара."""
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    face_cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
    )
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
    return tuple(faces)


def blur_faces(image: cv2.Mat, faces: Tuple[Tuple[int, int, int, int], ...]) -> cv2.Mat:
    """Размывает найденные лица на изображении."""
    for (x, y, w, h) in faces:
        face_roi = image[y:y+h, x:x+w]
        blurred = cv2.GaussianBlur(face_roi, (99, 99), 30)
        image[y:y+h, x:x+w] = blurred
    return image


def save_image(image: cv2.Mat, path: str) -> None:
    """Сохраняет изображение на диск."""
    cv2.imwrite(path, image)


if __name__ == "__main__":
    input_path = "/Users/macbook/PycharmProjects/scripts_edu/face_blur/img/train.jpg"
    output_path = "img/blurred_faces.jpg"

    img = load_image(input_path)
    found_faces = detect_faces(img)

    print(f"👀 Найдено лиц: {len(found_faces)}")

    blurred_img = blur_faces(img, found_faces)
    save_image(blurred_img, output_path)

    print(f"✅ Сохранено: {output_path}")