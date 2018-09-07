import sys
import tkinter as tk
from tkinter import messagebox
from tkinter import Toplevel
from .rooms import RoomsWindow
from .reserve import ReserveWindow
from .cancel import CancelWindow
from .price import PriceWindow
from .reservations import ReservationsWindow


class MenuWindow(tk.Toplevel):

    def __init__(self):
        tk.Toplevel.__init__(self)

        self.grid()
        self.title("Menu")
        self.geometry("150x170")
        self.create_widgets_menu()
        self.protocol("WM_DELETE_WINDOW", sys.exit)

    def create_widgets_menu(self):

        def open_rooms_window():
            rooms_window = RoomsWindow()

        def open_reserve_window():
            reserve_window = ReserveWindow()

        def open_cancel_window():
            cancel_window = CancelWindow()

        def open_price_window():
            price_window = PriceWindow()

        def open_reservations_window():
            price_window = ReservationsWindow()

        self.reserve_bttn = tk.Button(
            self, text="Reserve", command=open_reserve_window)
        self.reserve_bttn.grid(row=0, column=0)

        self.cancel_bttn = tk.Button(
            self, text="Cancel", command=open_cancel_window)
        self.cancel_bttn.grid(row=1, column=0)

        self.rooms_bttn = tk.Button(
            self, text="Rooms", command=open_rooms_window)
        self.rooms_bttn.grid(row=4, column=0)

        self.cancel_bttn = tk.Button(
            self, text="Price", command=open_price_window)
        self.cancel_bttn.grid(row=5, column=0)

        self.cancel_bttn = tk.Button(
            self, text="Reservations", command=open_reservations_window)
        self.cancel_bttn.grid(row=6, column=0)
