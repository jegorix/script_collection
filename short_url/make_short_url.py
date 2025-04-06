'''
Сокращай длинные ссылки в одну строку с помощью Python

Слишком длинный URL? Просто прогоняй через Python и получай миниатюрную ссылку за секунду.
🧠 Используем pyshorteners + TinyURL.
📥 Удобно для email, телеги, резюме, QR-кодов.
💡 Крутая фича для своих утилит, ботов и лендингов.

👨‍💻 Что делает код:
➡️ Запрашивает у пользователя любую ссылку;
➡️ С помощью библиотеки pyshorteners сокращает её через сервис TinyURL;
➡️ Выводит короткий вариант — удобно для социальных сетей, мессенджеров и email-рассылок.

pip install pyshorteners
'''

import pyshorteners

def shorten_link(link: str) -> str:
    """Сокращает ссылку с помощью TinyURL."""
    shortener = pyshorteners.Shortener()
    return shortener.tinyurl.short(link)

if __name__ == "__main__":
    user_link = input("🔗 Введите ссылку для сокращения: ").strip()
    try:
        result = shorten_link(user_link)
        print("✅ Сокращённая ссылка:", result)
    except Exception as e:
        print("❌ Ошибка при сокращении:", e)