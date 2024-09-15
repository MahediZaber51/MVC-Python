from sqlalchemy import Column, String, Integer, Float, ForeignKey,Boolean,DateTime,Text,Date
from database.db import BaseModel, session
from sqlalchemy.orm import relationship
from app.Models.balance import Balance # Import the Balance model
from datetime import datetime
# Define the Users model class, inheriting from BaseModel
class Users(BaseModel):
    __tablename__ = 'users' # Define the table name

    # Define the columns of the Users model
    name = Column(String, index=True,nullable=True) # Define the name column
    username = Column(String,unique=True, index=True,nullable=True) # Define the username column
    discord_id = Column(Integer, unique=True, index=True,nullable=True) # Define the discord_id column
    
    email = Column(String, unique=True, index=True,nullable=False) # Define the email column
    password = Column(String ,nullable=False) # Define the password column
    
    is_admin = Column(Boolean, default=False) # Define the is_admin column
    created_at = Column(DateTime,default= datetime.now()) # Define the created_at column
    updated_at = Column(DateTime,default= datetime.now()) # Define the updated_at column
    
    # Define a relationship to the Balance model
    balances = relationship('Balance', backref='user', cascade='all, delete-orphan')


    # Define a string representation for the Users model
    def __repr__(self):
        return f"<User(name={self.name}, email={self.email})>"
    
    # Define a method to get the user's balance
    def get_balance(self):
        """Get the user's balance, creating one if it doesn't exist."""
        if not self.balances:
            new_balance = Balance(user_id=self.id, amount=0.0)
            session.add(new_balance)
            session.commit()
            return new_balance
        return self.balances[0]

    # Define a method to deposit an amount to the user's balance
    def deposit(self, amount):
        """Deposit an amount to the user's balance."""
        balance = self.get_balance()
        balance.amount += amount
        session.commit()

    # Define a method to withdraw an amount from the user's balance
    def withdraw(self, amount):
        """Withdraw an amount from the user's balance."""
        balance = self.get_balance()
        if balance.amount >= amount:
            balance.amount -= amount
            session.commit()
        else:
            raise ValueError("Insufficient balance")