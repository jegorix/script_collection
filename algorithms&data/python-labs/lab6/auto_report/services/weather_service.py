import sys
from pathlib import Path
import requests
import pandas as pd
from datetime import datetime

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.append(str(ROOT))

from config import WEATHER_API_URL, WEATHER_API_KEY, DEFAULT_CITY

def fetch_weather(city: str | None = None, timeout: int = 10) -> pd.DataFrame:
    """Запрашивает текущую погоду для города и возвращает DataFrame с одной строкой."""
    if city is None:
        city = DEFAULT_CITY
        
    if not WEATHER_API_KEY:
        raise RuntimeError("API key for OpenWeatherMap not set. Put your key into config.WEATHER_API_KEY")
    
    params = {
        "q": city,
        "appid": WEATHER_API_KEY,
        "units": "metric",
        "lang": "ru"
    }
    
    resp = requests.get(WEATHER_API_URL, params=params, timeout=timeout)
    resp.raise_for_status()
    data = resp.json()
    
    main = data.get('main', {})
    weather_list = data.get("weather", [])
    wind = data.get("wind", {})
    
    row = {
        "Дата": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "Город": city,
        "Температура_С": main.get("temp"),
        "Ощущается_С": main.get("feels_like"),
        "Погода": weather_list[0].get('description') if weather_list else None,
        "Влажность_%": main.get("humidity"),
        "Ветер_м_с": wind.get("speed")
    }
    
    df = pd.DataFrame([row])
    
    return df