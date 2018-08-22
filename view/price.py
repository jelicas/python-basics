import tkinter as tk
from controller.queries import *
from controller.functions import get_info_about_price


class PriceWindow(tk.Toplevel):

    def __init__(self):
        tk.Toplevel.__init__(self)

        self.grid()
        self.title("Price of reservation")
        self.geometry("300x300")
        self.create_widgets_cancel()

    def create_widgets_cancel(self):
        s = Session()

        def show_price():
            if(ent_id.get() == ''):
                tk.messagebox.showinfo(
                    "Reservation", "You must enter reservation id.")
                return
            try:
                id = int(ent_id.get())
            except ValueError:
                tk.messagebox.showinfo(
                    "Reservation", "You must enter valid id.")
                return

            message = get_info_about_price(int(ent_id.get()), s)
            tk.messagebox.showinfo(
                "Reservation", message)

        lbl_id = tk.Label(self, text="Reservation id ")
        lbl_id.grid(row=0, column=0)

        ent_id = tk.Entry(self)
        ent_id.grid(row=0, column=1)

        bttn_submit = tk.Button(self, text="Submit", command=show_price)
        bttn_submit.grid(row=1, column=1)

    # private copy of original method
    __create_widgets_cancel = create_widgets_cancel
