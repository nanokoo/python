from tkinter import *

form = Tk()
form.title("Calculate roots of Quadratic equation")
txta = StringVar()
z = 0


def adding():
    a = float(E1.get())
    b = float(E2.get())
    c = float(E3.get())
    z = abs(b ** 2 - 4 * a * c)
    x1 = (-b + z) / (2 * a)
    x2 = (-b - z) / (2 * a)
    txta.set(str(x1) + " or " + str(x2))


L1 = Label(form, text="Value A")
L1.place(x=10, y=10)
E1 = Entry(form, bd=2)
E1.place(x=120, y=10)
L2 = Label(form, text="Value B")
L2.place(x=10, y=50)
E2 = Entry(form, bd=2)
E2.place(x=120, y=50)
L3 = Label(form, text="Value C")
L3.place(x=10, y=90)
E3 = Entry(form, bd=2)
E3.place(x=120, y=90)
L4 = Label(form, text="X is ")
L4.place(x=10, y=150)
E4 = Entry(form, bd=2, textvariable=txta)
E4.place(x=60, y=150)
B=Button (form, text= "solve,", bg='black',fg='white', command=lambda :adding())
B.place(x=100, y=200)
form.geometry("400x400")
form.mainloop()
