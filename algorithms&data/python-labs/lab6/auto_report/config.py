
"""Конфигурация проекта"""

# апи
EXCHANGE_API_URL = "https://v6.exchangerate-api.com/v6/"
EXCHANGE_API_KEY = "e3627b0f51bcbf399f8a57c4"
WEATHER_API_URL = "https://api.openweathermap.org/data/2.5/weather"
WEATHER_API_KEY = "60df5caa0b880580fcc637509dbe92ac" 

# Параметры по умолчанию
DEFAULT_CITY = "Minsk"
CURRENCY_BASE = "USD"
CURRENCY_SYMBOLS = ["EUR", "BYN", "RUB"]

# Пути к отчётам
REPORTS_DIR = "reports"
CURRENCY_FILE = f"{REPORTS_DIR}/currency_report.xlsx"
WEATHER_FILE = f"{REPORTS_DIR}/weather_report.xlsx"