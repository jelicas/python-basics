import tkinter as tk
from controller.queries import *


class CancelWindow(tk.Toplevel):

    def __init__(self):
        tk.Toplevel.__init__(self)

        self.grid()
        self.title("Cancel reservation")
        self.geometry("300x300")
        self.create_widgets_cancel()

    def create_widgets_cancel(self):
        s = Session()
        rooms = get_rooms(s)

        def cancel_res():
            cancel_reservation(int(ent_id.get()), s)
            tk.messagebox.showinfo(
                "Reservation", "Reservation has been canceled.")

        lbl_id = tk.Label(self, text="Reservation id ")
        lbl_id.grid(row=0, column=0)

        ent_id = tk.Entry(self)
        ent_id.grid(row=0, column=1)

        bttn_submit = tk.Button(self, text="Submit", command=cancel_res)
        bttn_submit.grid(row=1, column=1)
