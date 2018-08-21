from model.user import User
from model.room import Room
from model.reservation import Reservation
from controller.base import Session


def get_hotel_employee_un_and_pass(s):
    employees = s.query(User).all()

    # we want to create tuple of dictionaries, so we start with empty tuple
    employees_un_and_pass = ()

    # adding dictionary to tuple is actually creating new one each time
    # += compound operators
    for e in employees:
        un_and_pass = {'username': e.username, 'password': e.password}
        employees_un_and_pass += (un_and_pass,)

    return employees_un_and_pass


def get_rooms(s):
    rooms = s.query(Room).all()
    for r in rooms:
        print(r.id)

    return rooms


def get_room(id, s):
    room = s.query(Room).filter(Room.id == id).one()
    return room


def reserve_room(name, surname, id_card, date_from, date_to, id, s):
    room = get_room(id, s)

    reservation = Reservation(name, surname, id_card, date_from, date_to, room)

    s.add(reservation)
    s.commit()


def get_reservations(s):
    reservations = s.query(Reservation).all()
    for r in reservations:
        print(r.room_id)
    return reservations


def is_room_available(date_from, date_to, id, s):
    reservations = get_reservations(s)
    for r in reservations:
        if r.date_from == date_from or r.date_to == date_to or (r.date_from >= date_from and r.date_to <= date_to):
            return False
    return True


def cancel_reservation(id, s):
    deleted_res = s.query(Reservation).filter(
        Reservation.id == id).delete(synchronize_session=False)
    s.commit()
    print(deleted_res)


def get_reservation(id, s):
    res = s.query(Reservation).filter(Reservation.id == id).one()
    return res


session = Session()
result = cancel_reservation(4, session)
