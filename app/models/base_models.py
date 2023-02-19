from sqlalchemy import Column, Integer, Sequence

from app.entrypoint.database import Base


class BaseOrmModel(Base):
    __abstract__ = True
    
    id = Column(Integer, primary_key=True)
    