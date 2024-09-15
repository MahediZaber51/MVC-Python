import os
from sqlalchemy import create_engine, Column, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

DATABASE_URL = os.environ.get("DATABASE_URL")

engine = create_engine(DATABASE_URL)
SessionLocal = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class BaseModel(Base):
    __abstract__ = True

    id = Column(Integer, primary_key=True, index=True)

    @classmethod
    def create(cls, db_session, **kwargs):
        instance = cls(**kwargs)
        db_session.add(instance)
        db_session.commit()
        db_session.refresh(instance)
        return instance

    @classmethod
    def get(cls, db_session, id):
        return db_session.query(cls).filter(cls.id == id).first()

    @classmethod
    def all(cls, db_session):
        return db_session.query(cls).all()

    @classmethod
    def update(cls, db_session, id, **kwargs):
        instance = db_session.query(cls).filter(cls.id == id).first()
        if instance:
            for key, value in kwargs.items():
                setattr(instance, key, value)
            db_session.commit()
            db_session.refresh(instance)
        return instance

    @classmethod
    def delete(cls, db_session, id):
        instance = db_session.query(cls).filter(cls.id == id).first()
        if instance:
            db_session.delete(instance)
            db_session.commit()
        return instance

    @classmethod
    def filter(cls, db_session, **kwargs):
        query = db_session.query(cls)
        for key, value in kwargs.items():
            query = query.filter(getattr(cls, key) == value)
        return query.all()