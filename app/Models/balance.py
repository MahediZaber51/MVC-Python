from sqlalchemy import Column, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
from database.db import BaseModel

# Define the Balance model class, inheriting from BaseModel
class Balance(BaseModel):
    __tablename__ = 'balances'  # Define the table name

    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)  # Define the user_id column with a foreign key
    amount = Column(Float, nullable=False)  # Define the amount column

    # Define a string representation for the Balance model
    def __repr__(self):
        return f"<Balance(user_id={self.user_id}, amount={self.amount})>"
