from datetime import datetime
from decimal import Decimal
from typing import Optional, Union
from pydantic import BaseModel, ConfigDict, Field


class DeliveryDetailBase(BaseModel):
    user_id: int
    milkman_id: int
    date_time: Optional[datetime] = None
    quantity: int
    price: Union[Decimal, float]
    delivery_status: str = "pending"


class DeliveryDetailCreate(DeliveryDetailBase):
    pass


class DeliveryDetailUpdate(BaseModel):
    user_id: Optional[int] = None
    milkman_id: Optional[int] = None
    date_time: Optional[datetime] = None
    quantity: Optional[int] = None
    price: Optional[Union[Decimal, float]] = None
    delivery_status: Optional[str] = None


class DeliveryDetailResponse(DeliveryDetailBase):
    id: int

    model_config = ConfigDict(from_attributes=True)


DeliveryDetail = DeliveryDetailResponse