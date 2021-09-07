from sqlalchemy import (
    Column, Integer, String, Boolean, Date, Float)
from datetime import datetime, date
from ..database import Base


class CustomersDataFromClient(Base):
    __tablename__ = 'customers_data'

    id = Column(Integer, index=True, primary_key=True)
    email = Column(String(50), unique=True)
    monthly_earning_value = Column(Float(precision=2), nullable=False)
    date = Column(Date(), index=True, nullable=False)

