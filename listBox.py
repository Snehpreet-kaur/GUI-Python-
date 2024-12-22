from tkinter  import *

root = Tk()
root.title("My Favorite Games")

listbox = Listbox(root,height=10,width=15,bg="grey",activestyle='dotbox',font="Cursive",fg="yellow")

root.geometry ("300x250")

label= Label(root, text = "Favourite Games")

listbox.insert(1,"Fortnite")
listbox.insert(2,"Roblox")
listbox.insert(3,"Minecraft")
listbox.insert(4,"Super Mario")

label.pack()
listbox.pack()

root.mainloop()
