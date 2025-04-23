'''
убираем фон с любой картинки за пару секунд
Скрипт-проект на базе библиотеки rembg:
Открывает файл;
Убирает фон;
Сохраняет готовое изображение.

pip install rembg
pip install onnxruntime
'''

from rembg import remove


def remove_background(input_path: str, output_path: str) -> None:
    """Удаляет фон с изображения и сохраняет результат."""
    with open(input_path, 'rb') as input_file:
        with open(output_path, 'wb') as output_file:
            image_bytes: bytes = input_file.read()
            output_bytes: bytes = remove(image_bytes)
            output_file.write(output_bytes)

if __name__ == "__main__":
    remove_background('/Users/macbook/PycharmProjects/scripts_edu/remove_background/images/cap.jpg', '/Users/macbook/PycharmProjects/scripts_edu/remove_background/images/output.jpg')