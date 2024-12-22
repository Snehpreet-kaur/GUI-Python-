from tkinter import *

top = Tk()
top.title("Choose template")
top.geometry("450x300")
top.config(background="teal")

# the label for picking template
template= Label(top,text="Pick a template").place(x=40,y=60)
template_name= Entry(top,width=30).place(x=150,y=60)

# the label for naming project
project = Label(top,text="Name your project").place(x=40,y=100)
user_project = Entry(top,width=30).place(x=150,y=100)

submit_button = Button(top,text="Create REPL").place(x=150,y=130)

top.mainloop()