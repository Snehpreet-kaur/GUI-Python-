
from tkinter import *
# Create a GUI window
root = Tk()
root.config(background="teal")
# Function to convert weight
# given in kg to grams, pounds and ounces
def from_kg():
    # convert kg to gram
    gram = float(e2_value.get()) * 1000
    # convert kg to pound
    pound = float(e2_value.get()) * 2.20462
    # convert kg to ounce
    ounce = float(e2_value.get()) * 35.274
    # Enters the converted weight to
    # the text widget
    t1.delete("1.0", END)
    t1.insert(END, gram)
    t2.delete("1.0", END)
    t2.insert(END, pound)
    t3.delete("1.0", END)
    t3.insert(END, ounce)


# Create the Label widgets
e1 = Label(root, text="Enter the weight in Kg")
e2_value = StringVar()
e2 = Entry(root, textvariable=e2_value)
e3 = Label(root, text='Gram')
e4 = Label(root, text='Pounds')
e5 = Label(root, text='Ounce')

# Create the Text Widgets
t1 = Text(root, height=1, width=20)
t2 = Text(root, height=1, width=20)
t3 = Text(root, height=1, width=20)

# Create the Button Widget
b1 = Button(root, text="Convert", command=from_kg)

# grid method is used for placing
# the widgets at respective positions
# in table like structure
e1.grid(row=0, column=0)
e2.grid(row=0, column=1)
e3.grid(row=1, column=0)
e4.grid(row=1, column=1)
e5.grid(row=1, column=2)
t1.grid(row=2, column=0)
t2.grid(row=2, column=1)
t3.grid(row=2, column=2)
b1.grid(row=0, column=2)

# Start the GUI
root.mainloop()
