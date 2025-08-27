from fpdf import FPDF
from pathlib import Path
from typing import List


def images_to_pdf(images: List[str], output: str = "output.pdf") -> None:
    """
    Конвертирует список изображений в единый PDF-файл.

    :param images: список путей к изображениям (JPG, PNG и т.д.)
    :param output: имя выходного PDF-файла 
    """
    pdf = FPDF()

    for img_path in images:
        if not Path(img_path).exists():
            print(f"⚠️ Файл не найден: {img_path}")
            continue

        pdf.add_page()
        pdf.image(img_path, x=10, y=10, w=180)  # подгоняем ширину под страницу

    pdf.output(output)
    print(f"✅ PDF создан: {output}")


if __name__ == "__main__":
    # Пример использования
    images_to_pdf(
        ["from_img_to_pdf/images/image1.png", "from_img_to_pdf/images/image2.png", "from_img_to_pdf/images/image3.png"],

    )