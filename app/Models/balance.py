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
    
# Example usage of the Balance model

# Create a new balance instance for a user with user_id 1
# balance = Balance.create(user_id=1, amount=100.0)

# Get a balance instance by ID
# balance_instance = Balance.get(balance.id)
# print(balance_instance)  # Output: <Balance(user_id=1, amount=100.0)>

# Get all balance instances
# all_balances = Balance.all()
# print(all_balances)  # Output: [<Balance(user_id=1, amount=100.0)>]

# Update a balance instance by ID
# updated_balance = Balance.update(balance.id, amount=150.0)
# print(updated_balance)  # Output: <Balance(user_id=1, amount=150.0)>

# Delete a balance instance by ID
# deleted_balance = Balance.delete(balance.id)
# print(deleted_balance)  # Output: <Balance(user_id=1, amount=150.0)>

# Filter balance instances by user_id
# filtered_balances = Balance.filter(user_id=1)
# print(filtered_balances)  # Output: [<Balance(user_id=1, amount=150.0)>]

# Check if a balance instance exists by ID
# exists = Balance.exists(balance.id)
# print(exists)  # Output: True