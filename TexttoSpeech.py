#Import required modules
from tkinter import *
from gtts import gTTS

#module that helps to play the converted audio
import os

root=Tk()

frame1= Frame(root,bg="lightpink",height="150")
frame1.pack(fill=X)

frame2=Frame(root,bg="hotpink",height="750")
frame2.pack(fill=X)

label=Label(frame1,text="Text to Speech",font="bold,30",bg="lightpink")
label.place(x=180, y=70)

entry=Entry(frame2,width=45,bd=4,font=14)
entry.place(x=130, y=52)
entry.insert(0,"")

def play():
    language = "en"

    myobj = gTTS(text=entry.get(),lang=language,slow=False)
    myobj.save("convert.wav")
    os.system("convert.wav")

btn=Button(frame2, text="SUBMIT",width = "15", pady= 10, font= "bold, 15",command=play, bg="purple")
btn.place(x=250,y=130)

root.title("Text_to_Speech_Convertor")
root.geometry("650x550+350+200")

root.mainloop()