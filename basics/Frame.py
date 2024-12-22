from tkinter import * 

root = Tk()
root.geometry("300x150")

w=Label(root, text= 'IceCreams', font="50")
w.pack()

frame=Frame(root)
frame.pack()

bottomframe=Frame(root)
bottomframe.pack(side=LEFT)

b1_button= Button(frame,text="Choco",fg="red",bg="beige")
b1_button.pack(side=LEFT)

b2_button=Button(frame,text="Dark Choco",fg="brown", bg="beige")
b2_button.pack(side=LEFT)

b3_button=Button(frame,text="White Choco",fg="teal",bg="beige")
b3_button.pack(side=LEFT)

b4_button=Button(bottomframe,text="Strawberry",fg="turquoise",bg="cyan")
b4_button.pack(side=BOTTOM)

b5_button=Button(bottomframe,text="Butterscotch",fg="darkblue",bg="lightblue")
b5_button.pack(side=BOTTOM)

b6_button=Button(bottomframe,text="Strawberry",fg="red",bg="pink")
b6_button.pack(side=BOTTOM)

root.mainloop()
