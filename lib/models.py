import datetime
from pydantic import BaseModel


class Transaction(BaseModel):
    stock: str
    stock_amount: float
    stock_price: str
    when: datetime.datetime

