from pydantic import BaseModel
from enum import Enum
from typing import Optional

class Gender(str, Enum):
    male = "Male"
    female = "Female"

class Customer(BaseModel):
    account_number: int
    first_name: str
    last_name: str
    gender: Gender
    email: str
    balance: int
    is_premium: bool

class CustomerUpdateRequest(BaseModel):
    first_name: Optional[str]
    last_name: Optional[str]
    gender: Optional[Gender]
    email: Optional[str]
    balance: Optional[int]
    is_premium: Optional[bool]