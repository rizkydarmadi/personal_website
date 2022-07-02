from sqlalchemy import Column, ForeignKey, Integer, String,DateTime
from models import Base


class Content(Base):
    __tablename__ = "content"

    id = Column(Integer, primary_key=True, nullable=False)
    content_type = Column('content_type',ForeignKey('jenis_content.id'))
    create_by = Column('create_by',ForeignKey('user.id'))
    content = Column(String)
    created_date = Column('created_date', DateTime(timezone=True), nullable=False)
    updated_date = Column('updated_date', DateTime(timezone=True))