import argparse
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent
if str(ROOT) not in sys.path:
    sys.path.append(str(ROOT))
    
    
from services.currency_service import fetch_rates
from services.weather_service import fetch_weather
from utils.file_manager import append_to_excel, ensure_reports_dir
import config

def run_currency():
    df = fetch_rates()
    append_to_excel(config.CURRENCY_FILE, df)
    print("Курсы сохранены в:", config.CURRENCY_FILE)
    print(df.to_markdown(index=False))
    
def run_weather(city: str | None = None):
    df = fetch_weather()
    append_to_excel(config.WEATHER_FILE, df)
    print("Погода сохранена в:", config.WEATHER_FILE)
    print(df.to_markdown(index=False))
    
    
def main():
    # далее логика обработки документов командной строки
    parser = argparse.ArgumentParser(description="AutoReport: погода и курсы валют") #  --help.
    
    # добавил поддержку доп команд currency, weather, all
    sub = parser.add_subparsers(dest='command') # запишется в arg.command
    
    # доб доп команд
    
    # pogoda + gorod
    weather_p = sub.add_parser("weather", help="Получить погоду и сохранить в Excel")
    weather_p.add_argument("--city", "-c", help="Город для запроса погоды", default=None)
    
    # valuta
    sub.add_parser("currency", help="Получить курс валют и сохранить в Excel")
    
    # run all
    sub.add_parser("all", help="Сделать оба отчёта")
    
    # parse args
    args = parser.parse_args()
    
    
    ensure_reports_dir(config.REPORTS_DIR)
    
    if args.command == "currency":
        run_currency()
    elif args.command == "weather":
        run_weather(args.city)
    elif args.command == "all":
        run_currency()
        run_weather(None)
    else:
        parser.print_help()
        

if __name__ == "__main__":
    main()
    