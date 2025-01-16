from sqlalchemy import Column, ForeignKey, Integer, String, Boolean, Float
from sqlalchemy.orm import relationship
from app.backend.db import Base

class User(Base):
    __tablename__ = 'users'
    __table_args__ = {'keep_existing': True}

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, nullable=False)
    firstname = Column(String, nullable=True)
    lastname = Column(String, nullable=True)
    age = Column(Integer, nullable=True)
    slug = Column(String, unique=True, index=True)

    tasks = relationship("Task", back_populates="user")

from sqlalchemy.schema import CreateTable
print(CreateTable(User.__table__))