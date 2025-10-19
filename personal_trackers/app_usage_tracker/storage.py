import json
from pathlib import Path
from typing import List
import pandas as pd
from models import AppUsageSchema, AppUsage 
from loguru import logger


DATA_FILE = Path("./app_usage_tracker/data/data.json")
LOG_FILE = Path("./app_usage_tracker/logs/logs.json")

logger.add(LOG_FILE, format="{time} {level} {message}",
           level="DEBUG", rotation="1 MB", compression="zip")


def load_app_usage_json(file_path: Path = DATA_FILE) -> List[AppUsage]:
    """Load app usage from json file"""
    if not file_path.exists():
        file_path.parent.mkdir(parents=True, exist_ok=True)
        file_path.touch()
        file_path.write_text("[]", encoding="utf-8")
        logger.info(f"File {file_path} has been successfully created")
        
    try:
        with file_path.open("r", encoding="utf-8") as file:
            data_list = json.load(file)
    except json.JSONDecodeError:
        logger.warning("Файл поврежден или пуст, возвращаю пустой список")
        return []
        
    app_usage_list: List[AppUsage] = []
    
    for item in data_list:
        try:
            schema = AppUsageSchema(**item)
            app_usage_list.append(schema.to_app_usage())
        except Exception as e:
            logger.error(f"Ошибка при чтении данных: {e}")
            
    logger.success("Данные успешно загружены")
            
    return app_usage_list
    
def save_app_usage_json(app_usage_list: List[AppUsage], file_path: Path = DATA_FILE):
    """Save app usage data to json file"""
    data_list = [item.to_dict() for item in app_usage_list]
    
    ids = [item.id for item in app_usage_list]
    if len(ids) != len(set(ids)):
        logger.warning("Найдены дублирующиеся ID")
    
    try:
        with file_path.open("w", encoding='utf-8') as file:
            json.dump(data_list, file, ensure_ascii=False, indent=4)
    except Exception as e:
        logger.error(f"Ошибка при сохранении данных: {e}")
        
    logger.success("Данные успешно сохранены")
    

def app_usage_data_to_dataframe(app_usage_list: List[AppUsage]) -> pd.DataFrame:
    """Convert App Usage List to pandas DataFrame"""
    df = pd.DataFrame([item.to_dict() for item in app_usage_list])
    df["date"] = pd.to_datetime(df["date"])
    logger.success("Данные успешно преобразованы в pandas DataFrame")
    return df
    
    
if __name__ == "__main__":
    from datetime import datetime
    from models import Category
    
    schema = AppUsageSchema(
    app='Telegram',
    category=Category("Social"),
    minutes=20,
    date=datetime.now(),
    comment="Some comment"
)
    transaction = schema.to_app_usage()
    save_app_usage_json([transaction])
    data = load_app_usage_json()
    print(data)
    df_data = app_usage_data_to_dataframe(data)
    print(df_data)