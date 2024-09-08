import tkinter
from tkinter import *
from textblob import TextBlob


def check_spelling():
    word=enter_text.get()
    a=TextBlob(word)
    right=str(a.correct())

    c=Label(root,text="Correct Spelling:",font=("Arial",20),bg="#CAFF70",fg="#006400")
    c.place(x=100,y=250)
    spell.config(text=right)

root=Tk()
root.title("Spelling Checker Web")
root.geometry("700x400")
root.config(background="#CAFF70")


heading= Label(root,text="Spelling Checker",font=("Arial",30,"bold"),bg="#CAFF70",fg="#006400")
heading.pack(pady=(50,0))

enter_text=Entry(root,justify="center",width=30,font=("Arial",25),bg="white",border=2)
enter_text.pack(pady=10)
enter_text.focus()

button=Button(root,text="Check Spelling",font=("Arial",20,"bold"), fg="white",bg="#556B2F",command=check_spelling)
button.pack()
spell=Label(root,font=("Arial",20),bg="#CAFF70",fg="#006400")
spell.place(x=350,y=250)


root.mainloop()