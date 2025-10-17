from dataclasses import dataclass, field
from enum import Enum
from datetime import date
from typing import Optional

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
    amount: float
    category: Category
    type: TransactionType
    date: date
    comment: Optional[str] = field(default="")
