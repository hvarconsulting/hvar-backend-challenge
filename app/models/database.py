from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Set up the database engine and session factory
engine = create_engine("sqlite:///data/database.sqlite")
Session = sessionmaker(bind=engine)


def get_db_session():
    return Session()
