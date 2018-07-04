from tkinter import *
from tkinter import messagebox
from NoteDB import NoteDB
from dashboard import Dashboard
if __name__=="__main__":
    try:
        db=NoteDB()
        Dashboard().initUI(db)
    except Exception as e:
     messagebox.showinfo("Error","Unable to establish database connection.")