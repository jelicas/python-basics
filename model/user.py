from sqlalchemy import Column, String, Integer
from controller.base import Base


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    surname = Column(String(255))
    username = Column(String(255))
    password = Column(String(255))

    def __init__(self, name, surname, username, password):
        self.name = name
        self.surname = name
        self.username = username
        self.password = password
