from db import Base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from datetime import datetime

class Profiles(Base):
    __tablename__ = "Profiles"
    file_name = Column(String, primary_key=True)
    file_size = Column(Integer)
    creation_date = Column(DateTime)
    owner = Column(String)
    path = Column(String)

