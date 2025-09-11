import os
import time
import imaplib
import smtplib
import logging
from typing import Optional
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from email.utils import formatdate


"""
📩 Готовый скрипт, который:  
✔️ Создаёт письмо с HTML-телом и вложением.
✔️ Отправляет его через SMTP.
✔️ Сохраняет в папку "Отправленные".
✔️ Показывает логи в консоли и сохраняет их в файл.
✔️ Оборачивает всё в функции с обработкой ошибок.
"""


# Логгирование
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s — %(levelname)s — %(message)s",
    handlers=[
        logging.FileHandler("email_sender.log"),
        logging.StreamHandler()
    ]
)

def create_email(
    from_addr: str,
    to_addr: str,
    subject: str,
    body: str,
    attachment_path: Optional[str] = None
) -> MIMEMultipart:
    logging.info("Создание письма...")
    msg = MIMEMultipart()
    msg["From"] = from_addr
    msg["To"] = to_addr
    msg["Subject"] = Header(subject, 'utf-8')
    msg["Date"] = formatdate(localtime=True)
    msg.attach(MIMEText(body, 'html', 'utf-8'))

    if attachment_path and os.path.exists(attachment_path):
        try:
            part = MIMEBase('application', "octet-stream")
            with open(attachment_path, "rb") as file:
                part.set_payload(file.read())
            encoders.encode_base64(part)
            part.add_header(
                'Content-Disposition',
                f'attachment; filename="{os.path.basename(attachment_path)}"'
            )
            msg.attach(part)
            logging.info(f"Файл прикреплен: {attachment_path}")
        except Exception as e:
            logging.error(f"Ошибка при прикреплении файла: {e}")
    else:
        logging.warning("Файл не найден или не указан — письмо будет без вложения.")
    
    return msg

def send_email(
    smtp_server: str,
    smtp_port: int,
    from_addr: str,
    from_pass: str,
    to_addr: str,
    message: MIMEMultipart
) -> None:
    try:
        with smtplib.SMTP(smtp_server, smtp_port) as smtp:
            smtp.starttls()
            smtp.login(from_addr, from_pass)
            smtp.sendmail(from_addr, to_addr, message.as_string())
            logging.info(f"Письмо отправлено на {to_addr}")
    except Exception as e:
        logging.error(f"Ошибка отправки письма: {e}")

def save_to_sent(
    imap_server: str,
    imap_port: int,
    from_addr: str,
    from_pass: str,
    message: MIMEMultipart
) -> None:
    try:
        with imaplib.IMAP4(imap_server, imap_port) as imap:
            imap.login(from_addr, from_pass)
            imap.select('Sent')
            imap.append('Sent', None, imaplib.Time2Internaldate(time.time()), message.as_bytes())
            logging.info("Письмо сохранено в 'Sent'")
    except Exception as e:
        logging.error(f"Ошибка сохранения письма: {e}")

if __name__ == "__main__":
    FROM_EMAIL = "corp-mail@mail.ru"
    FROM_PASSWORD = "*"
    SMTP_SERVER = "*.mail.ru"
    SMTP_PORT = 25
    IMAP_PORT = 143
    TO_EMAIL = "students-mail@mail.ru"
    SUBJECT = "Тема сообщения"
    BODY = "Текст сообщения"
    ATTACHMENT_PATH = "сертификат.pdf"

    try:
        email_msg = create_email(FROM_EMAIL, TO_EMAIL, SUBJECT, BODY, ATTACHMENT_PATH)
        send_email(SMTP_SERVER, SMTP_PORT, FROM_EMAIL, FROM_PASSWORD, TO_EMAIL, email_msg)
        save_to_sent(SMTP_SERVER, IMAP_PORT, FROM_EMAIL, FROM_PASSWORD, email_msg)
    except Exception as e:
        logging.critical(f"Критическая ошибка: {e}")
