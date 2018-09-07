from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine(
    'mysql+pymysql://jelica:asus@localhost/sqlalchemy', echo=True)
#global scope
Session = sessionmaker(bind=engine)

Base = declarative_base()
