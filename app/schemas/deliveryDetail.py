from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Numeric
from datetime import datetime
from sqlalchemy.orm import relationship
from app.database.database import Base

class DeliveryDetail(Base):
    __tablename__ = "delivery_detail"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    milkman_id = Column(Integer, ForeignKey("milkman.id"), nullable=False)
    date_time = Column(DateTime, default=datetime.now, nullable=False)
    quantity = Column(Integer, nullable=False)
    price = Column(Numeric(10, 2), nullable=False)
    delivery_status = Column(String, nullable=False)
