from sqlalchemy import Column, Integer, String, DateTime
from models import Base

class email(Base):
    __tablename__ = "email"

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String)
    join_date = Column('created_date', DateTime(timezone=True), nullable=False)

