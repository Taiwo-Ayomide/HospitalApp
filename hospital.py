from tkinter import *
import sqlite3
from tkinter import messagebox

# Connect to the database 
conn = sqlite3.connect('database.db')
# print("Successful Connection")

c = conn.cursor()

# tkinter window

class Application:
    def __init__(self):
        self.root = Tk()
        self.root.title("Hospital Appointment")
        self.root.geometry("1200x720+0+0")
        self.root.resizable(False, False)


        #functions
        def add_appointment():
            
            F1 = Name.get()
            F2 = Age.get()
            F3 = Gender.get()
            F4 = Location.get()
            F5 = Phone.get()
            F6 = Time.get()

            if F1 == "" or F2 == "" or F3 == "" or F4 == "" or F5 == "" or F6 == "":
                messagebox.showerror("Hey", "Few information is missing")

            else:
                # Add to database
                sql = "INSERT INTO appointment (Name, Age, Gender, Location, phone, scheduled_time) VALUES(?,?,?,?,?,?)"
                c.execute(sql,(F1, F2, F3, F4, F5, F6))
                conn.commit()
                messagebox.showinfo("Success", "Appointment for " + str(F1) + " has been created")
                clear()
                # box.insert(END, "Appointment Fixed")
        
        def clear():
            Name.set('')
            Age.set('')
            Gender.set('')
            Location.set('')
            Phone.set('')
            Time.set('')

                

        # Frame
        left = Frame(self.root, width=800, height=700, bg='lightgreen').pack(side=LEFT)
        right = Frame(self.root, width=400, height=720, bg='steelblue').pack(side=RIGHT)
  


        # Heading
        Label(left, text="MASOC SPECIALIST HOSPITAL", font="Arial 39 bold", fg='black', bg='lightgreen').place(x=0, y=0)

        # Patient Name
        Label(left, text="Patient' Name", font='Arial 18 bold', fg='black', bg='lightgreen').place(x=0, y=100)

        # Age Name
        Label(left, text="Age", font='Arial 18 bold', fg='black', bg='lightgreen').place(x=0, y=140)

        # gender Name
        Label(left, text="Gender", font='Arial 18 bold', fg='black', bg='lightgreen').place(x=0, y=180)

        # Location 
        Label(left, text="Location", font='Arial 18 bold', fg='black', bg='lightgreen').place(x=0, y=220)

        # Phone time
        Label(left, text="Phone Number", font='Arial 18 bold', fg='black', bg='lightgreen').place(x=0, y=300)


        # Appointment time
        Label(left, text="Appointment Time", font='Arial 18 bold', fg='black', bg='lightgreen').place(x=0, y=260)



        # Text Entries
        Name=StringVar()
        name = Entry(left, width=30,  textvariable=Name).place(x=250, y=100)

        Age=StringVar()
        age = Entry(left, width=30, textvariable=Age).place(x=250, y=140)

        Gender=StringVar()
        gender = Entry(left, width=30, textvariable=Gender).place(x=250, y=180)

        Location=StringVar()
        location = Entry(left, width=30, textvariable=Location).place(x=250, y=220)

        Phone=StringVar()
        phone = Entry(left, width=30, textvariable=Phone).place(x=250, y=300)


        Time=StringVar()
        time = Entry(left, width=30, textvariable=Time).place(x=250, y=260)



        #Buttons
        Button(left, text="Add Appointment", width=20, height=2, bg='steelblue', font='Arial 14 bold', command=add_appointment).place(x=300, y=350)

        box = Text(right, width=44, height=30).place(x=820, y=30)


        self.root.mainloop()
Application()