from sqlalchemy import Column, String, Integer, Float, Boolean
from sqlalchemy.orm import relationship
from controller.base import Base


class Room(Base):
    __tablename__ = 'room'

    id = Column(Integer, primary_key=True)
    bed_number = Column(Integer)
    price = Column(Float)
    floor = Column(Integer)
    terrace = Column(Boolean)
    reservation = relationship("Reservation", back_populates="room")

    def __init__(self, bed_number, price, floor, terrace):
        self.bed_number = bed_number
        self.price = price
        self.floor = floor
        self.terrace = terrace
