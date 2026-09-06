from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Numeric
from datetime import datetime
from sqlalchemy.orm import relationship
from app.database.database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    phone_number = Column(String, nullable=False, unique=True ,index=True)
    address = Column(String, nullable=False)
    milkman_id = Column(Integer, ForeignKey("milkman.id"))
