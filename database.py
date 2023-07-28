from models import Customer, Gender
from typing import List
from uuid import UUID, uuid4

db: List[Customer] = [
    Customer(
        id=uuid4(),
        first_name="Piyush",
        last_name="Sharma",
        gender=Gender.male,
        email="piyushsharma220699@gmail.com",
        account_number=123456789102,
        balance=55000,
        is_premium=False
    ),
    Customer(
        id=uuid4(),
        first_name="Rohit",
        last_name="Sharma",
        gender=Gender.male,
        email="rohitsharma261203@gmail.com",
        account_number=734079774021,
        balance=75000,
        is_premium=True
    )
]