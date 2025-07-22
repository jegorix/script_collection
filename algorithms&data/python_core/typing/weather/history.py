from datetime import datetime
from pathlib import Path
import json

from weather_api_service import Weather
from weather_formatter import format_weather

from typing import TypedDict


class WeatherStorage:
    """Interface for any storage saving weather"""
    def save(self, weather: Weather) -> None:
        raise NotImplementedError
    
    
class HistoryRecord(TypedDict):
    date: str
    weather: str    

    
class JSONFileWeatherStorage(WeatherStorage):
    """Store weather in json file"""
    def __init__(self, jsonfile: Path):
        self._jsonfile = jsonfile
        self._init_storage()
        
    def save(self, weather: Weather) -> None:
        history = self._read_history()
        history.append(
            {
                "date": str(datetime.now()),
                "weather": format_weather(weather)
            }
        )
        self._write(history)
        
        
    def _init_storage(self) -> None:
        if not self._jsonfile.exists():
            self._jsonfile.write_text("[]")
            
    def _read_history(self) -> list[HistoryRecord]:
        with open(self._jsonfile, "r") as f:
            return json.load(f)
        
    def _write(self, history: list[HistoryRecord]) -> None:
        with open(self._jsonfile, "w") as f:
            json.dump(history, f, ensure_ascii=False, indent=4)
        
        
    
    
class PlainFileWeatherStorage(WeatherStorage):
    """Store weather in plain text file"""
    def __init__(self, file: Path):
        self._file = file
        
    def save(self, weather: Weather) -> None:
        now = datetime.now()
        formatted_weather = format_weather(weather)
        with open(self._file, "a") as f:
            f.write(f"{now}\n{formatted_weather}\n")
            
            
def save_weather(weather: Weather, storage: WeatherStorage) -> None:
    """Saves weather in the Storage"""
    storage.save(weather)