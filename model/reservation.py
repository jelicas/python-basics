from sqlalchemy import Column, String, Integer, Date, ForeignKey
from sqlalchemy.orm import relationship
from controller.base import Base


class Reservation(Base):
    __tablename__ = 'reservation'

    id = Column(Integer, primary_key=True)
    guest_name = Column(String(255))
    guest_surname = Column(String(255))
    guest_id_card = Column(Integer)
    date_from = Column(Date)
    date_to = Column(Date)
    room_id = Column(Integer, ForeignKey('room.id'))
    room = relationship("Room", back_populates="reservation")

    def __init__(self, guest_name, guest_surname, guest_id_card, date_from, date_to, room):
        self.guest_name = guest_name
        self.guest_surname = guest_surname
        self.guest_id_card = guest_id_card
        self.date_from = date_from
        self.date_to = date_to
        self.room = room
