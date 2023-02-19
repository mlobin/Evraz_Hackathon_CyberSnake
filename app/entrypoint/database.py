from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, Session, create_session

from .config import Settings

engine = None
Base = declarative_base()
SessionLocal: Session = scoped_session(lambda: create_session(autoflush=True, autocommit=True, bind=engine))
Base.query = SessionLocal.query_property()

def init_engines(settings: Settings):
    global engine
    global SessionLocal 
    engine = create_engine(settings.POSTGRES_DSN, pool_pre_ping=True)
    engine.dispose()
    return engine
