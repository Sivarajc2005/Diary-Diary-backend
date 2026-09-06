import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy_utils import create_database, database_exists
import app.models

load_dotenv()

user_name = os.getenv("DB_USER")
password = os.getenv("DB_PASSWORD")
port = os.getenv("DB_PORT")
database = os.getenv("DB_NAME")

engine = create_engine(f"postgresql://{user_name}:{password}@localhost:{port}/{database}")
session_maker = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

if not database_exists(engine.url):
    create_database(engine.url)
    Base.metadata.create_all(bind=engine)

def get_db():
    db = session_maker()
    try:
        yield db
    finally:
        db.close()






