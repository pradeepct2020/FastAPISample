from sqlalchemy import Column, String, Integer
from sqlalchemy.dialects.mysql import CHAR
import os
import sys
# Import local modules
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))

from app.db.database import Base
import uuid

class Customer(Base):
    __tablename__ = "customers"

    id = Column(CHAR(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    name = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    address = Column(String(255), nullable=True)



