from typing import Optional
from pydantic import BaseModel, ConfigDict


class PaymentDeliveriesBase(BaseModel):
    payment_id: int
    delivery_detail: int


class PaymentDeliveriesCreate(PaymentDeliveriesBase):
    pass


class PaymentDeliveriesUpdate(BaseModel):
    payment_id: Optional[int] = None
    delivery_detail: Optional[int] = None


class PaymentDeliveriesResponse(PaymentDeliveriesBase):
    id: int

    model_config = ConfigDict(from_attributes=True)


PaymentDeliveries = PaymentDeliveriesResponse
