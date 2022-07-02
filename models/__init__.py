from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

username = 'postgres'
password = '12qwaszx'
host = 'localhost'
port = 5435
database = 'ffnl'

engine = create_engine(
        f'postgresql+psycopg2://{username}:{password}@{host}:{port}/{database}'
    )

Session = sessionmaker(engine, future=True)

Base = declarative_base()

from .user import User
from .content import Content
from .jenisContent import jenisContent
from .emailList import email