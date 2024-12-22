from tkinter import *
import speech_recognition as sr
from tkinter.ttk import *
from tkinter import messagebox
from tkinter.filedialog import *

root = Tk()
root.title("Speech to Text")
root.geometry("800x400")

heading1 = Label(root,text="Voice Notepad", font = ("Cursive",30,"bold"))
heading1.grid(row=0, column=1, padx=20, pady=20)

label1= Label(root,text="Click button to record your speech:")
label1.grid(row=1, column=0, padx=10)

Output_text=Text(root, height=4, width=40)
Output_text.grid(row=1, column=1, pady=20, padx=20)

def Translate():
    r= sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak Anything")
        audio= r.listen(source)
        try:
            text=r.recognize_google(audio)
        except:
            text="Sorry could not recognize your voice"
        Output_text.delete(1.0, END)
        Output_text.insert(END, text)

def save():
    fout= asksaveasfile(defaultextension=".txt")
    if fout:
        print(Output_text.get(1.0,END), file= fout)
    else:
        messagebox.showinfo("Warning", "Text not saved")

trans_btn= Button(root, text="Click on me!!... \n To start recording", command=Translate)
trans_btn.grid(row=1, column=0, pady=20, padx=20)

save_btn= Button(root, text="Save the text", command=save)
save_btn.grid(row=1, column=2, pady=10, columnspan=3)

root.mainloop()
