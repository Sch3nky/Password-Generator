import random
import datetime
from tkinter import *

#variables

písmena = "abcdefghijklmnopqrstuvwxyz"
čísla = "1234567890"
znaky = "@&{}()_/Đ[]*"
velkáPísmena = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
all = písmena + velkáPísmena

passE = False

modes = [("Yes",1),
         ("No",0)]

fontsetting = 17

#window setting

win = Tk()
win.title("Password generator")
win.maxsize(600,500)
win.geometry("600x500")
win.configure(bg= "white")

#starting page canvas

canvas = Canvas(win)
canvas.place(x=175, y = 175)
canvas.configure(bg = "white", highlightcolor="white", highlightbackground="white")

#function adding numbers and symbols to password

def ST():
    global all
    if all.find(znaky) != 52:
        all = all + znaky

def SF():
    global all
    global znaky
    x = all.replace(znaky,"")
    all = x

def NT():
    global all
    if all.find(čísla) != 52:
        all = all + čísla

def NF():
    global all
    global čísla
    x = all.replace(čísla,"")
    all = x

#function that generate password and control password setting

def PasswordGen():
    length = lengthBox.get()
    global passE

    try:
        if int(length) > 30:
            lengthBox.configure(bg="#ff0000")
        elif length.isnumeric(): 
            lengthBox.configure(bg="#99aab5")
            password1 = "".join(random.sample(all, int(length)))
            password2 = "".join(random.sample(all, int(length)))
            password3 = "".join(random.sample(all, int(length)))        

            passE = True 
            passwordL1 = Label(passwordCan, text=password1, bg="white", font=("Mozer Heavy",15))
            passwordL2 = Label(passwordCan, text=password2,bg="white", font=("Mozer Heavy",15))
            passwordL3 = Label(passwordCan, text=password3,bg="white", font=("Mozer Heavy",15))
            passwordL1.grid(row=0, columnspan=3,sticky=NSEW)
            passwordL2.grid(row=1, columnspan=3,sticky=NSEW)
            passwordL3.grid(row=2, columnspan=3,sticky=NSEW)
    except:
        lengthBox.configure(bg="#ff0000")

#main function that create main canvas and destroy starting canvas

def F():
    canvas.destroy()

    #main canvas
    global mainCanvas
    mainCanvas = Canvas(win)
    mainCanvas.place(x=20, y = 10)
    mainCanvas.configure(bg = "white", highlightcolor="white", highlightbackground="white")
    
    global passwordCan
    passwordCan = Canvas(mainCanvas)
    passwordCan.grid(row=4,column=3,columnspan=4, rowspan=8)

    passwordL1 = Label(passwordCan, text="",bg="white", font=(13))
    passwordL2 = Label(passwordCan, text="",bg="white", font=(13))
    passwordL3 = Label(passwordCan, text="",bg="white", font=(13))
    passwordL1.grid(row=0, columnspan=3,sticky=NSEW)
    passwordL2.grid(row=1, columnspan=3,sticky=NSEW)
    passwordL3.grid(row=2, columnspan=3,sticky=NSEW)


    #Password setting
    setting = Label(mainCanvas, text=b"Password Setting",font= ("Lucida",25), bg= "white", fg="#242424")
    setting.grid(row=0, columnspan=3,sticky=NSEW)
    
    #password length

    lengthL = Label(mainCanvas, text="Password length",bg= "white", font=("Verdana",fontsetting))
    lengthL.grid(row=1, column=0, sticky=SW)

    global lengthBox
    lengthBox = Spinbox(mainCanvas, from_=6, to=25, bg="#b4b3ba", font=("Console",15))
    lengthBox.grid(row=2,columnspan=3, sticky=N)

    #numbers in password

    numbersL = Label(mainCanvas, text="Numbers",font=("Verdana",fontsetting), bg="white")
    numbersL.grid(row=3,column=0, sticky=SW)
    
    global nNo
    global sNo
    nNo = IntVar()
    nNo.set(0)
    sNo = IntVar()
    sNo.set(0)
    rowM = 3

    for i,j in modes:
        rowM += 1
        numbersRB = Radiobutton(mainCanvas, text=i, variable=nNo, value=j, bg="white") 
        numbersRB.grid(row=rowM,column=0, sticky=NSEW)
        if rowM == 3:
            numbersRB.config(command=NF)
        else:
            numbersRB.config(command=NT)

    #symbols in password

    symbolsL = Label(mainCanvas, text="Symbols", font=("Verdana",fontsetting), bg="white")
    symbolsL.grid(row=6,column=0, sticky=SW)

    rowM = 6
    for i,j in modes:
        rowM += 1
        symbolRB = Radiobutton(mainCanvas, text=i, variable=sNo, value=j, bg="white") 
        symbolRB.grid(row=rowM,column=0, sticky=NSEW)
        if rowM == 3:
            symbolRB.config(command=SF)
        else:
            symbolRB.config(command=ST)
    
    #Password and empty space labels

    password = Label(mainCanvas, text="Password", font=("Lucida",25),bg="white")
    password.grid(row=0,column=3, columnspan=3, sticky=W+E, padx=50)
    
    space2 = Label(mainCanvas, text="     ", font=(40), bg = "white")
    space2.grid(row=1,column=5)

    space3 = Label(mainCanvas, text="     ", font=(20), bg = "white")
    space3.grid(row=0,column=3)

    #generate Button

    generateB = Button(mainCanvas, text="Generate", command=PasswordGen,font=(14), bg = "#240f0f", fg="white", width = 15, height = 2)
    generateB.grid(row=2,column=4,padx=55)



welcome = Label(canvas, text=b"Password generator", font=("Intro Medium", 20), bg = "white")
welcome.grid(columnspan = 3, row=0)

space1 = Label(canvas, text=" ", font=(20), bg = "white")
space1.grid(columnspan = 3, row=2)
space2 = Label(canvas, text="Created by Jakub Schenk", font=("Hero light",10), bg = "white")
space2.grid(columnspan = 3, row=1)

start= Button(canvas, text="Start", font = ("Arial", 20), command=F,height = 1, width = 10, bg="#36393f", fg="#e1dedc", )
start.grid(column = 1, row=3)

#mailoop


win.mainloop()


