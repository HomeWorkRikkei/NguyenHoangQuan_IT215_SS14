from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from sqlalchemy_utils import create_database, database_exists

DATABASE_URL = 'mysql+pymysql://API_db:123456@localhost:3306/fast_api_db'
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

class Base(DeclarativeBase): pass

def init_db():
    if not database_exists(engine.url):
        create_database(engine.url)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()