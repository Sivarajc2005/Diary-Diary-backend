from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Numeric
from datetime import datetime
from sqlalchemy.orm import relationship
from app.database.database import Base

class Payment(Base):
    __tablename__ = "payment_table"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    milkman_id = Column(Integer, ForeignKey("milkman.id"))
    payment_amount = Column(Numeric(10, 2), nullable=False)
    payment_date = Column(DateTime, default=datetime.now, nullable=False)
    payment_method = Column(String, nullable=False)
    transaction_id = Column(String, nullable=True, default=None)
    payment_status = Column(String, nullable=False)
