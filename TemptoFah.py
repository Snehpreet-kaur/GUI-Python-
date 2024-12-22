from tkinter import *
import tkinter.font as font

root = Tk()
root.title("Celsius to Fahrenheit Converter")
root.config(background="teal")

d= Label(root, text="Celsius --> Fahrenheit",font=("Comic Sans MS",20,"bold"), bg="teal", fg="white")
d.pack()

frame= Frame(root)
frame.pack(padx=5, pady=20)

m= Label(frame, text="Enter temperature in Celsius: ", font=("Comic Sans MS",10),bg="teal")
m.grid(row=0, column=0 )

c=Entry(frame, font=("Comic Sans MS",10))
c.grid(row=0, column=1 ) 

e= Label(frame, text=" Please enter valid input..",font=("Comic Sans MS",10),fg="red")

o= Label(frame, font=("Comic Sans MS",10), bg= "teal", fg="white")
o.grid(row=2, column=0, columnspan=2, pady=10)

submit = Button(frame, text="Convert", width=30, font=("Comic Sans MS",10),bg="cyan")
submit.grid(row=3, column=0, columnspan=2, pady=10)


root.mainloop()