# imports
from datetime import date
from .base import engine, Base, Session
from model.user import User
from model.room import Room
from model.reservation import Reservation


# schema
Base.metadata.create_all(engine)

# session
session = Session()

# users
jeca = User("Jelica", "Stanojevic", "jeca", "jeca123")
mika = User("Milica", "Miljkovic", "mika", "mika123")

# rooms
room1 = Room(1, 50.0, 1, False)
room2 = Room(2, 80.0, 1, False)
room3 = Room(3, 100.0, 1, False)
room11 = Room(1, 60.0, 2, True)
room22 = Room(2, 90.0, 2, True)
room33 = Room(3, 110.0, 2, True)
room111 = Room(1, 60.0, 3, True)
room222 = Room(2, 90.0, 3, True)
room333 = Room(3, 110.0, 3, True)

# reservations
res1 = Reservation("Maja", "Nikolic", 111111111, date(
    2018, 8, 20), date(2018, 8, 25), room1)
res2 = Reservation("Uros", "Velickovic", 222222222,
                   date(2018, 9, 20), date(2018, 9, 25), room22)
res3 = Reservation("Milunka", "Djokic", 333333333, date(
    2018, 10, 20), date(2018, 10, 25), room33)

session.add(jeca)
session.add(mika)

session.add(room1)
session.add(room2)
session.add(room3)
session.add(room11)
session.add(room22)
session.add(room33)
session.add(room111)
session.add(room222)
session.add(room333)

session.add(res1)
session.add(res2)
session.add(res3)

session.commit()
session.close()

"""docker run --name pythonBasics \
    -e POSTGRES_PASSWORD=passs \
    -e POSTGRES_USER=ussr \
    -e POSTGRES_DB=sqlalchemy \
    -p 5433:5433 \
    -d postgres"""
