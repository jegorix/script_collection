from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from typing import Optional, Dict, Any
from uuid import uuid4
from pydantic import BaseModel, Field, field_validator



class Category(Enum):
    WORK = "Work"
    ENTERTAINMENT = "Entertainment"
    SOCIAL = "Social"
    OTHER = "Other"
    

@dataclass
class AppUsage:
    id: str = field(default_factory=lambda: str(uuid4()))
    app: str = "Browser"
    category: Category = Category.OTHER
    minutes: int = 1
    date: datetime = Field(default_factory=datetime.now)
    comment: Optional[str] = ""
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert object to json dict"""
        return {
            "id": self.id,
            "app": self.app,
            "category": self.category.value, 
            "minutes": self.minutes,
            "date": self.date.isoformat(),
            "comment": self.comment
        }
        
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "AppUsage":
        # Create new AppUsage object from json dict
        category_str = data.get("category", "Other")
        category = Category(category_str.capitalize())
        
        date_str = data.get("date", datetime.now().isoformat())
        date = datetime.fromisoformat(date_str)
        
        return cls(
            id=data.get("id", str(uuid4())),
            app=data.get("app", "Browser"),
            category=category,
            minutes=data.get("minutes", 1),
            date=date,
            comment=data.get("comment", "")
        )
    
    
class AppUsageSchema(BaseModel):
    """Pydantic model for AppUsage Validation"""
    id: Optional[str] = Field(default=None)
    app: str = Field(...)
    category: Category = Field(...)
    minutes: int = Field(...)
    date: datetime = Field(...)
    comment: Optional[str] = Field(default="")
    
    @field_validator("minutes")
    def minutes_must_be_positive(cls, value: int) -> int:
        if value < 0:
            raise ValueError("Minutes must be positive")
        return value
    
    def to_app_usage(self) -> AppUsage:
        return AppUsage(
            id=self.id or str(uuid4()),
            app=self.app,
            category=self.category,
            minutes=self.minutes,
            date=self.date,
            comment=self.comment or ""
        )
        
        
        
if __name__ == '__main__':
    schema = AppUsageSchema(
        app='Telegram',
        category=Category("Social"),
        minutes=20,
        date=datetime.now(),
        comment="Some comment"
    )
    transaction = schema.to_app_usage()
    print(f"AppUsage transaction: {transaction}")
    print(f"AppUsage transaction to dict: {transaction.to_dict()}")