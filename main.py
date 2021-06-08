from tkinter import *
import tkinter
window = tkinter.Tk()
window.title("SPR")
window.configure(background="#fff")
# user controls
ButtonFrame = Frame(window, width=600, height=200)
ButtonFrame.pack(side=BOTTOM)

Scissors = Button(ButtonFrame, text="Scissors", width=10,
                  cursor="dotbox", relief=RIDGE)
Paper = Button(ButtonFrame, text="Paper", width=10,
               cursor="spider", relief=RIDGE)
Rock = Button(ButtonFrame, text="Rock", width=10,
              cursor="pirate", relief=RIDGE)

Scissors.grid(column=0, row=0, padx=20)
Paper.grid(column=1, row=0, padx=20)
Rock.grid(column=2, row=0, padx=20)

# window.configure(bg="#ffff")
window.geometry("700x400")
window.mainloop()
