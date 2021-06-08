from tkinter import *
import tkinter
from PIL import Image, ImageTk

window = tkinter.Tk()
window.title("SPR")
window.configure(background="#fff")

# adding Image
paper = ImageTk.PhotoImage(Image.open('paper.png'))
paperUser = ImageTk.PhotoImage(Image.open('paper-user.png'))
rock = ImageTk.PhotoImage(Image.open('rock.png'))
rockUser = ImageTk.PhotoImage(Image.open('rock-user.png'))
scissors = ImageTk.PhotoImage(Image.open('scissors-user.png'))
scissorsUser = ImageTk.PhotoImage(Image.open('scissors.png'))


# user controls
ButtonFrame = Frame(window, width=600, height=300)
ButtonFrame.pack(side=BOTTOM, fill="x")
for i in range(3):
    ButtonFrame.grid_columnconfigure(i, weight=1)

Scissors = Button(ButtonFrame, text="Scissors", width=10,
                  cursor="dotbox", relief=RIDGE)
Paper = Button(ButtonFrame, text="Paper", width=10,
               cursor="spider", relief=RIDGE)
Rock = Button(ButtonFrame, text="Rock", width=10,
              cursor="pirate", relief=RIDGE)

# visual area
VisualFrame = Frame(window, width=700, height=700)
VisualFrame.pack(side=TOP, fill="x")
VisualFrame.configure(background="black")
for i in range(2):
    VisualFrame.grid_columnconfigure(i, weight=1)

compMove = Button(VisualFrame, text="Computer :", width=10)
userMove = Label(VisualFrame, text="Player 1 :", width=10)
compMove.grid(column=0, row=0)
userMove.grid(column=1, row=0)


computerMoveFrame = Frame(
    VisualFrame, height=100, width=100)
humanMoveFrame = Frame(
    VisualFrame,  height=100, width=100)
computerMoveFrame.grid(column=0, row=1)
humanMoveFrame.grid(column=1, row=1)

panel = Label(computerMoveFrame, image=paper)
panel.pack()
panel = Label(humanMoveFrame, image=paper)
panel.pack()


Scissors.grid(column=0, row=0)
Paper.grid(column=1, row=0)
Rock.grid(column=2, row=0)

# window.resizable(0, 0)
window.geometry("900x400")
window.mainloop()
