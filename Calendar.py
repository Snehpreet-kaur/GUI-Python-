#import all methods and classes from tkinter
from tkinter import * 
#import calendar module
import calendar

#function for showing the calendar of the given year
def showCal():
    #create a root window
    root = Tk()
    #set the background colour of the root window
    root.config(background="hotpink")
    #set the name of tkinter root window
    root.title("CALENDAR")
    #set the configuration of the root window
    root.geometry("550x600")

    #get method returns current text as string
    fetch_year=int(year_field.get())

    #calendar method of the calendar module to return the calendar of the given year
    cal_content = calendar.calendar(fetch_year)

    #create a label for showing the content of calendar
    cal_year = Label(root, text=cal_content, font="Consolas 10 bold")

    #grid method for placing the widgets at respective positions in table like structures
    cal_year.grid(row=5 , column=1, padx =20)

    root.mainloop()

#driver code
if __name__ == "__main__":
    #create a root window
    root=Tk()
     #set the background colour of the root window
    root.config(background="orange")
    #set the name of tkinter root window
    root.title("CALENDAR")
    #set the configuration of the root window
    root.geometry("250x140")

    #create a calendar
    cal=Label(root, text="CALENDAR",bg="turquoise",font=("Cursive",28,'bold'))
    #create a "enter year "label
    year=Label(root, text="Enter Year", bg="cyan")

    #create a text entry box for filling or typing the information
    year_field=Entry(root)

    #create a button and attach to the previous function
    Show= Button(root, text="Show Calendar", fg="Black", bg="Teal",command=showCal)

    #create an exit button
    Exit=Button(root,text="Exit",fg="black",bg="orange",command=exit)

    cal.pack()
    year.pack()
    year_field.pack()
    Show.pack()
    Exit.pack()



    root.mainloop()



