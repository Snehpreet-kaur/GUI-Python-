from tkinter import *

root = Tk()

root .geometry("500x500")
root.title("basics")

thing=Button(root,text="CLICK ME..",bd='6',background="teal",command=root.destroy)
thing.pack(side='top')

root.mainloop()