import os
from sqlalchemy import create_engine, Column, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

# Get the database URL from environment variables
DATABASE_URL = os.environ.get("DATABASE_URL")

# Create the SQLAlchemy engine
engine = create_engine(DATABASE_URL)

# Create a configured "Session" class
SessionLocal = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))

# Create a base class for declarative class definitions
Base = declarative_base()

# Dependency to get the database session
def get_db():
    """
    Dependency to get the database session.
    
    Yields:
        Session: The database session.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Base model class with common methods for all models
class BaseModel(Base):
    """
    Base model class with common methods for all models.
    
    Attributes:
        __abstract__ (bool): Indicates that this class will not be mapped to a table in the database.
        id (int): The primary key of the model.
    """
    __abstract__ = True  # This class will not be mapped to a table in the database

    id = Column(Integer, primary_key=True, index=True)  # Every model will have an id column

    @classmethod
    def create(cls, db_session, **kwargs):
        """
        Create a new instance of the model and add it to the session.

        Args:
            db_session (Session): The database session.
            **kwargs: The attributes of the model.

        Returns:
            BaseModel: The created instance of the model.
        """
        instance = cls(**kwargs)
        db_session.add(instance)
        db_session.commit()
        db_session.refresh(instance)
        return instance

    @classmethod
    def get(cls, db_session, id):
        """
        Get an instance of the model by ID.

        Args:
            db_session (Session): The database session.
            id (int): The ID of the model instance.

        Returns:
            BaseModel: The instance of the model, or None if not found.
        """
        return db_session.query(cls).filter(cls.id == id).first()

    @classmethod
    def all(cls, db_session):
        """
        Get all instances of the model.

        Args:
            db_session (Session): The database session.

        Returns:
            list: A list of all instances of the model.
        """
        return db_session.query(cls).all()

    @classmethod
    def update(cls, db_session, id, **kwargs):
        """
        Update an instance of the model by ID with the given keyword arguments.

        Args:
            db_session (Session): The database session.
            id (int): The ID of the model instance.
            **kwargs: The attributes to update.

        Returns:
            BaseModel: The updated instance of the model, or None if not found.
        """
        instance = db_session.query(cls).filter(cls.id == id).first()
        if instance:
            for key, value in kwargs.items():
                setattr(instance, key, value)
            db_session.commit()
            db_session.refresh(instance)
        return instance

    @classmethod
    def delete(cls, db_session, id):
        """
        Delete an instance of the model by ID.

        Args:
            db_session (Session): The database session.
            id (int): The ID of the model instance.

        Returns:
            BaseModel: The deleted instance of the model, or None if not found.
        """
        instance = db_session.query(cls).filter(cls.id == id).first()
        if instance:
            db_session.delete(instance)
            db_session.commit()
        return instance

    @classmethod
    def filter(cls, db_session, **kwargs):
        """
        Filter instances of the model by the given keyword arguments.

        Args:
            db_session (Session): The database session.
            **kwargs: The attributes to filter by.

        Returns:
            list: A list of instances of the model that match the filter criteria.
        """
        query = db_session.query(cls)
        for key, value in kwargs.items():
            query = query.filter(getattr(cls, key) == value)
        return query.all()
    
    @classmethod
    def exists(cls, db_session, id):
        """
        Check if an instance of the model exists by ID.

        Args:
            db_session (Session): The database session.
            id (int): The ID of the model instance.

        Returns:
            bool: True if the instance exists, False otherwise.
        """
        return db_session.query(cls).filter(cls.id == id).exists()