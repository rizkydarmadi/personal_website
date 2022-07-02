from sqlalchemy import Column, ForeignKey, Integer, String,Boolean, DateTime
from models import Base

class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String)
    password = Column(String)
    is_superuser = Column(Boolean)
    join_date = Column('created_date', DateTime(timezone=True), nullable=False)

    # permissioon_id = ''