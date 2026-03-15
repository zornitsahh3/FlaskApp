from sqlalchemy import Column, Integer, String, DateTime
from database import Base
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime,timezone

Base = declarative_base()

class Todo(Base):
    __tablename__="todos"

    id=Column(Integer,primary_key=True,index=True)
    text=Column(String,nullable=False)
    
class User(Base):
    __tablename__='users'

    id=Column(Integer,primary_key=True)
    username=Column(String(80),unique=True,nullable=False)
    email=Column(String(120),unique=True,nullable=False)
    password_hash=Column(String(255),nullable=False)
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    
    def __repr__(self):
        return f'<User {self.username}>'