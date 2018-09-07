import tkinter as tk
from controller.queries import *
from controller.config import s


class RoomsWindow(tk.Toplevel):

    def __init__(self):
        tk.Toplevel.__init__(self)

        self.grid()
        self.title("Rooms")
        self.geometry("300x300")
        self.create_widgets_rooms()

    def create_widgets_rooms(self):
        rooms = get_rooms(s)
        i = 1

        l1 = tk.Label(self, text='id    ', relief=tk.RIDGE)
        l1.grid(row=0, column=0, sticky=tk.NSEW)
        l2 = tk.Label(self, text='bed number', relief=tk.RIDGE)
        l2.grid(row=0, column=1, sticky=tk.NSEW)
        l3 = tk.Label(self, text='floor   ', relief=tk.RIDGE)
        l3.grid(row=0, column=2,  sticky=tk.NSEW)
        l4 = tk.Label(self, text='price    ', relief=tk.RIDGE)
        l4.grid(row=0, column=3, sticky=tk.NSEW)
        l5 = tk.Label(self, text='terrace   ', relief=tk.RIDGE)
        l5.grid(row=0, column=4, sticky=tk.NSEW)

        # printf-style String Formatting
        for r in rooms:
            l1 = tk.Label(self, text='%s' %
                          (str(r.id)+"       "), relief=tk.RIDGE)
            l1.grid(row=i, column=0, sticky=tk.NSEW)
            l2 = tk.Label(self, text='%s' %
                          (str(r.bed_number)+"      "), relief=tk.RIDGE)
            l2.grid(row=i, column=1, sticky=tk.NSEW)
            l3 = tk.Label(self, text='%s' %
                          (str(r.floor)+"      "), relief=tk.RIDGE)
            l3.grid(row=i, column=2,  sticky=tk.NSEW)
            l4 = tk.Label(self, text='%s' %
                          (str(r.price)+"      "), relief=tk.RIDGE)
            l4.grid(row=i, column=3, sticky=tk.NSEW)
            l5 = tk.Label(self, text='%s' %
                          (str(r.terrace)+"      "), relief=tk.RIDGE)
            l5.grid(row=i, column=4, sticky=tk.NSEW)
            i += 1
