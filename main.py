from tkinter import *

t = 0
# function set_timer
def set_timer():
    global t
    t = t+int(e1.get())
    return t

# function countdown
def countdown():
    global t
    if t > 0:
        l1.config(text=t)
        t = t-1
        l1.after(1000, countdown)
    elif t == 0:
        print("End")
        l1.config(text="Goo")


# Create the UI
root = Tk()
root.geometry("180x150")

# number for the countdown
l1 = Label(root, font="times 20")
l1.grid(row=1, column=2)

# input from user
times = StringVar()
e1 = Entry(root, textvariable=times)
e1.grid(row=3, column=2)

# button to set
bSet = Button(root, text="SET", width=20, command=set_timer)
bSet.grid(row=4, column=2, padx=20)

# button to start
bStart = Button(root, text="START", width=20, command=countdown)
bStart.grid(row=5, column=2, padx=20)

root.mainloop()
