from sqlalchemy import Column, String
from database.db import BaseModel

class Users(BaseModel):
    __tablename__ = 'users'

    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)

    def __repr__(self):
        return f"<User(name={self.name}, email={self.email})>"