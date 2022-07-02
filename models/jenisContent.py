from sqlalchemy import Column, Integer, String
from . import Base

class jenisContent(Base):
    __tablename__ = "jenis_content"

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String)
