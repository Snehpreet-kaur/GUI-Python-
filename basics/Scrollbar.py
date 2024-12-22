from tkinter import * 

root = Tk()
root.geometry("150x200")

w=Label(root,text="Hello",font=('Comic Sans MS',50))
w.pack()

scroll_Bar=Scrollbar(root)
scroll_Bar.pack(side=RIGHT,fill=Y)

mylist=Listbox(root,yscrollcommand=scroll_Bar.set)

for line in range(1,26):
    mylist.insert(END, "Hi "+str(line))

mylist.pack(side=LEFT,fill=BOTH)

scroll_Bar.config(command=mylist.yview)

root.mainloop()
