from tkinter import *
from Web.Connexion.Sql import Sql

class WindowConnection:

    """
    Cette classe permet de creer la fenetre de connection et de se connecter a la base de donnee
    """

    def __init__(self) -> None:
        Sql.open_bdd()
        self.window = Tk()
        self.window.resizable(False, False)
        size = (400, 250)
        self.window.title("Connection")
        self.window.geometry(str(size[0]) + "x" + str(size[1]))
        self.window.minsize(size[0], size[1])
        self.color = '#C0C0C0'
        self.window.config(bg=self.color)
        self.frame = Frame(self.window, bg=self.color)
        self.frame2= Frame(self.window, bg=self.color)
        menu = Menu(self.window)

        self.LoginInput = Entry(self.frame, width=30)
        self.LoginInput.grid(column=2,row=1)
        LabelName = Label(self.frame, font=('Arial Black', 15), text='Login :', width=9, height=1, background=self.color, anchor=E)
        LabelName.grid(column=1, row=1)

        Space = Label(self.frame, height=1, background=self.color)
        Space.grid(column = 1, row = 2)

        self.PasswordInput = Entry(self.frame, width=30)
        self.PasswordInput.grid(column=2,row=3)
        LabelPassword = Label(self.frame, font=('Arial Black', 15), text='Password :', width=9, height=1, background=self.color, anchor=E)
        LabelPassword.grid(column=1, row=3)

        FinishButton = Button(self.frame2, font = ('Arial Black', 15), text='Connection', width=15, height=2, command=self.apply)
        FinishButton.grid(column=1, row=1)

        self.frame.pack(expand=YES)
        self.frame2.pack(expand=YES)
        self.window.config(menu= menu)
        self.window.mainloop()

    def apply(self):
        retour = Sql.connection(self.LoginInput.get(), self.PasswordInput.get())
        if not retour:
            self.LoginInput.delete(0, END)
            self.PasswordInput.delete(0, END)
        else:
            self.window.quit()
            self.window.destroy()