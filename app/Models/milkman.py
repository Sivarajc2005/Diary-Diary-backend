from typing import Optional
from pydantic import BaseModel, ConfigDict


class MilkmanBase(BaseModel):
    name: str
    phone_number: str
    address: str


class MilkmanCreate(MilkmanBase):
    pass


class MilkmanUpdate(BaseModel):
    name: Optional[str] = None
    phone_number: Optional[str] = None
    address: Optional[str] = None


class MilkmanResponse(MilkmanBase):
    id: int

    model_config = ConfigDict(from_attributes=True)


Milkman = MilkmanResponse
MilkMan = MilkmanResponse