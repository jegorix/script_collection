import json
from pathlib import Path
from typing import List
import pandas as pd
from models.transaction import Transaction, TransactionSchema

DATA_FILE = Path("data/data.json")


def load_transaction_json(file_path: Path = DATA_FILE) -> List[Transaction]:
    if not file_path.exists():
        return []
    with file_path.open("r", encodin="utf-8") as file:
        data_list = json.load(file)

    transactions: List[Transaction] = []
    for item in data_list:
        try:
            schema = TransactionSchema(**item)
            transactions.append(schema.to_trasaction())
        except Exception as e:
            print(f"Ошибка при чтении транзакции: {e}")

    return transactions


def save_transactions_json(
    transactions: List[Transaction], file_path: Path = DATA_FILE
) -> None:
    """Save list of transactions to json file"""
    data_list = [transaction.to_dict() for transaction in transactions]
    with file_path.open("w", encoding="utf-8") as file:
        json.dump(data_list, file, ensure_ascii=False, indent=4)


def transaction_to_dataframe(transactions: List[Transaction]) -> pd.DataFrame:
    df = pd.DataFrame([transaction.to_dict() for transaction in transactions])
    df["date"] = pd.to_datetime(df["date"])
    return df


if __name__ == "__main__":
    print("Success")
