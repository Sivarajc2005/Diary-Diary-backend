from datetime import datetime
from decimal import Decimal
from typing import Optional, Union
from pydantic import BaseModel, ConfigDict


class PaymentBase(BaseModel):
    user_id: int
    milkman_id: Optional[int] = None
    payment_amount: Union[Decimal, float]
    payment_date: Optional[datetime] = None
    payment_method: str
    transaction_id: Optional[str] = None
    payment_status: str


class PaymentCreate(PaymentBase):
    pass


class PaymentUpdate(BaseModel):
    user_id: Optional[int] = None
    milkman_id: Optional[int] = None
    payment_amount: Optional[Union[Decimal, float]] = None
    payment_date: Optional[datetime] = None
    payment_method: Optional[str] = None
    transaction_id: Optional[str] = None
    payment_status: Optional[str] = None


class PaymentResponse(PaymentBase):
    id: int

    model_config = ConfigDict(from_attributes=True)


Payment = PaymentResponse
