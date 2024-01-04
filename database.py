from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine(
    "postgresql://postgres:ES6iCYcms5XBK2!@localhost:5433/item_id", echo=True
)

Base = declarative_base()

SessionLocal = sessionmaker(bind=engine)
