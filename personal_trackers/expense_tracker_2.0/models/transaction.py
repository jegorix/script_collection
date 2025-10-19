from dataclasses import dataclass
from datetime import datetime
from enum import Enum
from typing import Optional, Dict, Any
from uuid import uuid4
from pydantic import BaseModel, Field, field_validator


class Category(Enum):
    FOOD = "Food"
    TRANSPORT = "Transport"
    RENT = "Rent"
    SALARY = "Salary"
    OTHER = "Other"


class TransactionType(Enum):
    INCOME = "Income"
    EXPENSE = "Expense"


@dataclass
class Transaction:
    id: str = Field(default_factory=lambda: str(uuid4()))
    amount: float = 0.0
    category: Category = Category.OTHER
    type: TransactionType = TransactionType.EXPENSE
    date: datetime = Field(default_factory=datetime.now)
    comment: Optional[str] = ""

    def to_dict(self) -> Dict[str, Any]:
        # Convert the Transaction object to a dictionary for pandas or json
        return {
            "id": self.id,
            "amount": self.amount,
            "category": self.category.value,
            "type": self.type.value,
            "date": self.date.isoformat(),
            "comment": self.comment,
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Transaction":
        # Create a new Transaction object from a dictionary
        
        category_str = data.get("category", "Other")
        category = Category(category_str)
        
        type_str = data.get("type", "Expense")
        type = TransactionType(type_str)
        
        date_str = data.get("date", datetime.now().isoformat())
        date = datetime.fromisoformat(date_str)
        
        return cls(
            id=data.get("id", str(uuid4())),
            amount=data.get("amount", 0.0),
            category=category,
            type=type,
            date=date,
            comment=data.get("comment", ""),
        )


class TransactionSchema(BaseModel):
    """Pydantic model for validation external data"""

    id: Optional[str] = Field(default=None)
    amount: float = Field(...)
    category: Category = Field(...)
    type: TransactionType = Field(...)
    date: datetime = Field(...)
    comment: Optional[str] = Field(default="")

    @field_validator("amount")
    def amount_must_be_finite(cls, v: float) -> float:
        if not (-1e6 < v < 1e6):
            raise ValueError("Amount must be finite")
        return v

    def to_transaction(self) -> Transaction:
        return Transaction(
            id=self.id or str(uuid4()),
            amount=self.amount,
            category=self.category,
            type=self.type,
            date=self.date, 
            comment=self.comment or "",
        )


if __name__ == "__main__":
    print("Hello World!")