from datetime import date
import tkinter as tk
from controller.queries import *
from controller.functions import *


class ReserveWindow(tk.Toplevel):

    def __init__(self):
        tk.Toplevel.__init__(self)

        self.grid()
        self.title("Reserve")
        self.geometry("300x300")
        self.create_widgets_reserve()

    def create_widgets_reserve(self):
        s = Session()

        def open_menu():
            self.destroy()

        def reserve():
            if(room_exists(int(ent_room.get()), s) == True):
                if(can_u_reserve_that_room(date(int(ent_year.get()), int(ent_month.get()), int(ent_day.get())), date(int(ent_year2.get()), int(ent_month2.get()), int(ent_day2.get())), int(ent_room.get()), s) == True):
                    tk.messagebox.showinfo("Room", "Room is available!")
                    reserve_room(ent_name.get(), ent_surname.get(), int(ent_id.get()), date(int(ent_year.get()), int(ent_month.get()), int(
                        ent_day.get())), date(int(ent_year2.get()), int(ent_month2.get()), int(ent_day2.get())), int(ent_room.get()), s)
                    create_mail(ent_name.get(), ent_surname.get(), int(ent_id.get()), date(int(ent_year.get()), int(ent_month.get()), int(
                        ent_day.get())), date(int(ent_year2.get()), int(ent_month2.get()), int(ent_day2.get())), int(ent_room.get()), s)
                else:
                    tk.messagebox.showinfo("Room", "Room is not available!")
            else:
                tk.messagebox.showinfo("Room", "Room does not exist!")

        lbl_name = tk.Label(self, text='Name ')
        lbl_name.grid(row=0, column=0)

        ent_name = tk.Entry(self)
        ent_name.grid(row=0, column=1)

        lbl_surname = tk.Label(self, text='Surname ')
        lbl_surname.grid(row=1, column=0)

        ent_surname = tk.Entry(self)
        ent_surname.grid(row=1, column=1)

        lbl_id = tk.Label(self, text='Id card ')
        lbl_id.grid(row=2, column=0)

        ent_id = tk.Entry(self)
        ent_id.grid(row=2, column=1)

        lbl_df = tk.Label(self, text='Date from ')
        lbl_df.grid(row=3, column=0)

        lbl_day = tk.Label(self, text='Day ')
        lbl_day.grid(row=3, column=1)
        ent_day = tk.Entry(self)
        ent_day.grid(row=3, column=2)

        lbl_month = tk.Label(self, text='Month ')
        lbl_month.grid(row=3, column=3)
        ent_month = tk.Entry(self)
        ent_month.grid(row=3, column=4)

        lbl_year = tk.Label(self, text='Year ')
        lbl_year.grid(row=3, column=5)
        ent_year = tk.Entry(self)
        ent_year.grid(row=3, column=6)

        lbl_dt = tk.Label(self, text='Date to ')
        lbl_dt.grid(row=4, column=0)

        lbl_day2 = tk.Label(self, text='Day ')
        lbl_day2.grid(row=4, column=1)
        ent_day2 = tk.Entry(self)
        ent_day2.grid(row=4, column=2)

        lbl_month2 = tk.Label(self, text='Month ')
        lbl_month2.grid(row=4, column=3)
        ent_month2 = tk.Entry(self)
        ent_month2.grid(row=4, column=4)

        lbl_year2 = tk.Label(self, text='Year ')
        lbl_year2.grid(row=4, column=5)
        ent_year2 = tk.Entry(self)
        ent_year2.grid(row=4, column=6)

        lbl_room = tk.Label(self, text='Room id ')
        lbl_room.grid(row=5, column=0)

        ent_room = tk.Entry(self)
        ent_room.grid(row=5, column=1)

        submit_bttn = tk.Button(
            self, text="Submit", command=reserve)
        submit_bttn.grid(row=7, column=1, sticky=tk.W)

        menu_bttn = tk.Button(
            self, text="Menu", command=open_menu)
        menu_bttn.grid(row=8, column=1, sticky=tk.W)
