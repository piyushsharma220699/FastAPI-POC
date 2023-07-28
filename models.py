from pydantic import BaseModel
from enum import Enum
from typing import Optional
from uuid import UUID, uuid4

class Gender(str, Enum):
    male = "Male"
    female = "Female"

# class Address(BaseModel):
#     street: Optional[str]
#     city: Optional[str]
#     state: Optional[str]
#     country: str

class Customer(BaseModel):
    id: Optional[UUID] = uuid4()
    first_name: str
    last_name: str
    gender: Gender
    email: str
    # address: Optional[Address]
    account_number: int
    balance: int
    is_premium: bool