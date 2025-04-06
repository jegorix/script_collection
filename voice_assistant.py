'''
Скучно читать длинные PDF-документы? Python поможет.
С помощью библиотеки pyttsx3 и PyPDF2 можно легко превратить любой PDF в аудиокнигу,
которую ваш ПК будет зачитывать вслух.
'''

#pip install pyttsx3 PyPDF2

import pyttsx3
from PyPDF2 import PdfReader
from typing import Optional

def read_pdf_aloud(file_path: str, voice_id: Optional[int] = None, rate: int = 150) -> None:
    try:
        with open(file_path, 'rb') as file:
            pdf = PdfReader(file)
            speaker = pyttsx3.init()
            if voice_id is not None:
                voices = speaker.getProperty('voices')
                speaker.setProperty('voice', voices[voice_id].id)
            speaker.setProperty('rate', rate)

            for i, page in enumerate(pdf.pages):
                text = page.extract_text()
                if text:
                    print(f"\n📖 Чтение страницы {i+1}:\n{text[:]}...\n")
                    speaker.say(text)
                    speaker.runAndWait()

            speaker.stop()
    except Exception as e:
        print(f"Ошибка: {e}")

if __name__ == "__main__":
    read_pdf_aloud("files/example.pdf", voice_id=0)