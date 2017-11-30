from tkinter import *  # so i dont have to put tkinter. infront of everything


def closewindow():
    exit()

def ok():
    ok = Tk()
    ok.title("Well done")
    ok.geometry("150x150")
    okLabel = Label(ok, text="congrats!")  # command runs a function
    close = Button(ok, text="OK", command=closewindow)
    close.pack()
    okLabel.pack()  # putting this after to change order
    ok.mainloop()


def enterBox():
    box = Tk()
    box.title("Enter Box")
    box.geometry("150x150")
    v = StringVar()
    e = Entry(box, textvariable=v)
    e.pack()
    v.set(v.get())  # TODO: I GIVE UP!
    theyEntered = v.get()
    global theyEntered
    enterOK = Button(box, text="OK", command=new)
    enterOK.pack()
    box.mainloop()



def new():
    global theyEntered
    new = Tk()
    newLabel = Label(new, text=theyEntered)
    newLabel.pack()
    new.mainloop()

main = Tk()
main.title("Box Title")
main.geometry("300x300")
mainLabel = Label(main, text="close or click OK!")
mainLabel.pack()
closeButton = Button(main, text="Close", command=closewindow)
okButton = Button(main, text="OK", command=enterBox)
okButton.pack()
closeButton.pack()
main.mainloop()


"""
so...
tkinter.Tk creates a window under a variable
        .Button creates a button under a variable
        .Label creates text under a variable
	.Enter creates a text field
	.Text creates a large text field
variable.pack() puts the variable into the message box
"""
