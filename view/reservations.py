import tkinter as tk
from controller.queries import *


class ReservationsWindow(tk.Toplevel):

    def __init__(self):
        tk.Toplevel.__init__(self)

        self.grid()
        self.title("Reservations")
        self.geometry("600x300")
        self.create_widgets_reservations()

    def create_widgets_reservations(self):
        s = Session()
        reservations = get_reservations(s)
        i = 1

        l1 = tk.Label(self, text='id    ', relief=tk.RIDGE)
        l1.grid(row=0, column=0, sticky=tk.NSEW)
        l2 = tk.Label(self, text='guest name', relief=tk.RIDGE)
        l2.grid(row=0, column=1, sticky=tk.NSEW)
        l3 = tk.Label(self, text='guest surname', relief=tk.RIDGE)
        l3.grid(row=0, column=2,  sticky=tk.NSEW)
        l4 = tk.Label(self, text='guest id card', relief=tk.RIDGE)
        l4.grid(row=0, column=3, sticky=tk.NSEW)
        l5 = tk.Label(self, text='date from', relief=tk.RIDGE)
        l5.grid(row=0, column=4, sticky=tk.NSEW)
        l6 = tk.Label(self, text='date to', relief=tk.RIDGE)
        l6.grid(row=0, column=5, sticky=tk.NSEW)
        l7 = tk.Label(self, text='room id', relief=tk.RIDGE)
        l7.grid(row=0, column=6, sticky=tk.NSEW)

        # printf-style String Formatting
        for r in reservations:
            l1 = tk.Label(self, text='%s' %
                          (str(r.id)+"       "), relief=tk.RIDGE)
            l1.grid(row=i, column=0, sticky=tk.NSEW)
            l2 = tk.Label(self, text='%s' %
                          (str(r.guest_name)+"      "), relief=tk.RIDGE)
            l2.grid(row=i, column=1, sticky=tk.NSEW)
            l3 = tk.Label(self, text='%s' %
                          (str(r.guest_surname)+"      "), relief=tk.RIDGE)
            l3.grid(row=i, column=2,  sticky=tk.NSEW)
            l4 = tk.Label(self, text='%s' %
                          (str(r.guest_id_card)+"      "), relief=tk.RIDGE)
            l4.grid(row=i, column=3, sticky=tk.NSEW)
            l5 = tk.Label(self, text='%s' %
                          (str(r.date_from)+"      "), relief=tk.RIDGE)
            l5.grid(row=i, column=4, sticky=tk.NSEW)
            l6 = tk.Label(self, text='%s' %
                          (str(r.date_to)+"      "), relief=tk.RIDGE)
            l6.grid(row=i, column=5, sticky=tk.NSEW)
            l7 = tk.Label(self, text='%s' %
                          (str(r.room_id)+"      "), relief=tk.RIDGE)
            l7.grid(row=i, column=6, sticky=tk.NSEW)
            i += 1
