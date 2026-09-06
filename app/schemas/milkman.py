from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Numeric
from datetime import datetime
from sqlalchemy.orm import relationship
from app.database.database import Base

class Milkman(Base):
    __tablename__ = "milkman"
    id = Column(Integer, nullable=False, primary_key=True, index=True)
    name = Column(String, nullable=False)
    phone_number = Column(String, nullable=False, unique=True ,index=True)
    address = Column(String, nullable=False)