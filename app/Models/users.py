from sqlalchemy import Column, String, Integer, Float, ForeignKey, Boolean, DateTime, Text, Date
from database.db import BaseModel, session
from sqlalchemy.orm import relationship
from app.Models.balance import Balance  # Import the Balance model
from datetime import datetime

# Define the Users model class, inheriting from BaseModel
class Users(BaseModel):
    """
    Users model representing the users of the application.

    Attributes:
        __tablename__ (str): The name of the table in the database.
        name (str): The name of the user.
        username (str): The unique username of the user.
        discord_id (int): The unique Discord ID of the user.
        email (str): The unique email of the user.
        password (str): The password of the user.
        is_admin (bool): Indicates if the user is an admin.
        created_at (datetime): The timestamp when the user was created.
        updated_at (datetime): The timestamp when the user was last updated.
        balances (relationship): The relationship to the Balance model.
    """
    __tablename__ = 'users'  # Define the table name

    # Define the columns of the Users model
    name = Column(String, index=True, nullable=True)  # Define the name column
    username = Column(String, unique=True, index=True, nullable=True)  # Define the username column
    discord_id = Column(Integer, unique=True, index=True, nullable=True)  # Define the discord_id column
    email = Column(String, unique=True, index=True, nullable=False)  # Define the email column
    password = Column(String, nullable=False)  # Define the password column
    is_admin = Column(Boolean, default=False)  # Define the is_admin column
    created_at = Column(DateTime, default=datetime.now())  # Define the created_at column
    updated_at = Column(DateTime, default=datetime.now())  # Define the updated_at column

    # Define a relationship to the Balance model
    balances = relationship('Balance', backref='user', cascade='all, delete-orphan')

    def __repr__(self):
        """
        String representation of the Users model.

        Returns:
            str: A string representation of the Users instance.
        """
        return f"<User(name={self.name}, email={self.email})>"

    def get_balance(self):
        """
        Get the user's balance, creating one if it doesn't exist.

        Returns:
            Balance: The user's balance.
        """
        if not self.balances:
            new_balance = Balance(user_id=self.id, amount=0.0)
            session.add(new_balance)
            session.commit()
            return new_balance
        return self.balances[0]

    def deposit(self, amount):
        """
        Deposit an amount to the user's balance.

        Args:
            amount (float): The amount to deposit.
        """
        balance = self.get_balance()
        balance.amount += amount
        session.commit()

    def withdraw(self, amount):
        """
        Withdraw an amount from the user's balance.

        Args:
            amount (float): The amount to withdraw.

        Raises:
            ValueError: If the balance is insufficient.
        """
        balance = self.get_balance()
        if balance.amount >= amount:
            balance.amount -= amount
            session.commit()
        else:
            raise ValueError("Insufficient balance")
        
        
    def transfer(self, recipient, amount):
        """
        Transfer an amount from the user's balance to the recipient's balance.

        Args:
            recipient (Users): The recipient user.
            amount (float): The amount to transfer.

        Raises:
            ValueError: If the balance is insufficient.
        """
        balance = self.get_balance()
        if balance.amount >= amount:
            balance.amount -= amount
            recipient_balance = recipient.get_balance()
            recipient_balance.amount += amount
            session.commit()
        else:
            raise ValueError("Insufficient balance")
        
