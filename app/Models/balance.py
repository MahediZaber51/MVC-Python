from sqlalchemy import Column, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
from database.db import BaseModel

# Define the Balance model class, inheriting from BaseModel
class Balance(BaseModel):
    """
    Balance model representing the balance of a user.

    Attributes:
        __tablename__ (str): The name of the table in the database.
        user_id (int): Foreign key referencing the user's ID.
        amount (float): The balance amount.
    """
    __tablename__ = 'balances'  # Define the table name

    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)  # Define the user_id column with a foreign key
    amount = Column(Float, nullable=False)  # Define the amount column

    def __repr__(self):
        """
        String representation of the Balance model.

        Returns:
            str: A string representation of the Balance instance.
        """
        return f"<Balance(user_id={self.user_id}, amount={self.amount})>"