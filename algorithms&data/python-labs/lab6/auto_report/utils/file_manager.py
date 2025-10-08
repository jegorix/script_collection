from pathlib import Path
import pandas as pd

def ensure_reports_dir(path: str) -> None:
    Path(path).mkdir(parents=True, exist_ok=True)
    
def append_to_excel(file_path: str | Path, df: pd.DataFrame) -> None:
    """Добавляет строки из df в файл file_path (создаёт файл, если его нет)."""
    p = Path(file_path)
    
    ensure_reports_dir(p.parent)
    
    if p.exists():
        old = pd.read_excel(p, engine="openpyxl")
        new = pd.concat([old, df], ignore_index=True)
    else:
        new = df
        
    new.to_excel(p, index=False)