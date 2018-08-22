import sys
import tkinter as tk
from tkinter import messagebox
from controller.functions import *
from view.menu import MenuWindow

# inheriting


class LogInWindow(object):

    def __init__(self, parent):
        self.root = parent
        self.root.title("Log in")
        self.frame = tk.Frame(parent)
        self.frame.grid()
        self.create_widgets()
        self.s = Session()
        self.root.protocol("WM_DELETE_WINDOW", sys.exit)

    def hide(self):
        self.root.withdraw()

    def create_widgets(self):

        # inner function

        def check_user():
            if(can_u_log_in(self.un_ent.get(), self.pw_ent.get(), self.s) == True):
                print("Yes")
                tk.messagebox.showinfo("Log in", "Successfully logged in!")
                self.hide()
                menuFrame = MenuWindow(self.s)
            else:
                print("No")
                tk.messagebox.showinfo("Log in", "Wrong username or password!")
                self.un_ent.delete(0, tk.END)
                self.pw_ent.delete(0, tk.END)

        self.inst_lbl = tk.Label(
            self.frame, text="Enter password and username")
        self.inst_lbl.grid(row=0, column=0, columnspan=2, sticky=tk.W)

        self.un_lbl = tk.Label(self.frame, text="Username: ")
        self.un_lbl.grid(row=1, column=0, sticky=tk.W)

        self.un_ent = tk.Entry(self.frame)
        self.un_ent.grid(row=1, column=1, sticky=tk.W)

        self.pw_lbl = tk.Label(self.frame, text="Password: ")
        self.pw_lbl.grid(row=2, column=0, sticky=tk.W)

        self.pw_ent = tk.Entry(self.frame)
        self.pw_ent.grid(row=2, column=1, sticky=tk.W)

        self.submit_bttn = tk.Button(
            self.frame, text="Submit", command=check_user)
        self.submit_bttn.grid(row=3, column=1, sticky=tk.W)


if __name__ == '__main__':

    root = tk.Tk()
    root.geometry("250x100")
    app = LogInWindow(root)
    root.mainloop()


"""variable = Frame(root)

variable.pack(side=, fill=, fg=, bg=, sticky=)

variable = Button(frame, text=, fg, bg, command=)

label_two = Label(frame_two, text='Hello, tkinter!', fg ='blue', bg='white')
label_two.pack()

photo
"""
