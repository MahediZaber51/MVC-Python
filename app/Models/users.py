from sqlalchemy import Column, String
from database.db import BaseModel

# Define the Users model class, inheriting from BaseModel
class Users(BaseModel):
    __tablename__ = 'users' # Define the table name

    name = Column(String, index=True) # Define the name column
    email = Column(String, unique=True, index=True) # Define the email column
    password = Column(String) # Define the password column

    # Define a string representation for the Users model
    def __repr__(self):
        return f"<User(name={self.name}, email={self.email})>"