from services.storage import transaction_to_dataframe, load_transaction_json
from pathlib import Path


file = Path("data/test.json")

try:
    data = load_transaction_json(file_path=file)
    df_data = transaction_to_dataframe(data)
    
except FileNotFoundError:
    print("Файл не найден")
    
else:  
    print(df_data)
