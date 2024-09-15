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
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Base model class with common methods for all models
class BaseModel(Base):
    __abstract__ = True  # This class will not be mapped to a table in the database

    id = Column(Integer, primary_key=True, index=True) # Every model will have an id column

    @classmethod
    def create(cls, db_session, **kwargs):
        """
        Create a new instance of the model and add it to the session.
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
        """
        return db_session.query(cls).filter(cls.id == id).first()

    @classmethod
    def all(cls, db_session):
        """
        Get all instances of the model.
        """
        return db_session.query(cls).all()

    @classmethod
    def update(cls, db_session, id, **kwargs):
        """
        Update an instance of the model by ID with the given keyword arguments.
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
        """
        query = db_session.query(cls)
        for key, value in kwargs.items():
            query = query.filter(getattr(cls, key) == value)
        return query.all()