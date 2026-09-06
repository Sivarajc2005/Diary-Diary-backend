from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Numeric
from datetime import datetime
from sqlalchemy.orm import relationship
from app.database.database import Base

class PaymentDeliveries(Base):
    __tablename__ = "payment_deliveries"
    id = Column(Integer, nullable=False, primary_key=True)
    payment_id = Column(Integer,ForeignKey("payment_table.id") , nullable=True)
    delivery_detail = Column(Integer, ForeignKey("delivery_detail.id"), nullable=False)
    