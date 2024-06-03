import os
from sqlalchemy import (
    create_engine,
    Column,
    Integer,
    String,
    Numeric,
    Text,
    TIMESTAMP,
    PrimaryKeyConstraint,
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.schema import CreateSchema

variables = ["DB_HOST", "DB_PORT", "DB_USER", "DB_PASSWORD", "DB_DATABASE"]

# Check if any of the variables are missing in the environment
if any(variable not in os.environ for variable in variables):
    from dotenv import load_dotenv

    load_dotenv()

# These should now point to the ProxySQL service
DB_HOST = os.getenv("DB_HOST", "postgres")
DB_PORT = os.getenv("DB_PORT", 5432)
DB_USER = os.getenv("DB_USER", "postgres")
DB_PASSWORD = os.getenv("DB_PASSWORD", "postgres")
DB_DATABASE = os.getenv("DB_DATABASE", "postgres")

SQLALCHEMY_DATABASE_URL = (
    f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_DATABASE}"
)
# print(SQLALCHEMY_DATABASE_URL)

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


# Define the Logs table
class Logs(Base):
    __tablename__ = "logs"
    ids = Column(Text, primary_key=True)
    msg_datetime = Column(TIMESTAMP(timezone=True), primary_key=True)
    obj_track_id = Column(Integer)
    labels = Column(String(128))
    scores = Column(Numeric)
    left_coords = Column(Integer)
    upper_coords = Column(Integer)
    right_coords = Column(Integer)
    down_coords = Column(Integer)
    created_at = Column(TIMESTAMP(timezone=True))


# # Create the database if it does not exist
# if not engine.dialect.has_schema(engine, DB_DATABASE):
#     engine.execute(CreateSchema(DB_DATABASE))

# Create all tables
Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
