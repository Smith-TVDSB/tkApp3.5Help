import tkinter as tk #this shortens me writing tkinter to tk
from tkinter.constants import SUNKEN
from tkinter import messagebox

def questionA():
    #Make a function to check answer A (coded last)
    def checkAnswerA():
        #access score and its label
        global score, scoreLbl

        #If correctd
        if entryA.get().lower() == "blue":
            messagebox.showinfo("Question A","Correct!")
            #Updates score
            score += 1
            scoreLbl.config(text = "Score: "+ str(score))
            #Closes window afterwards
            windowA.destroy()
        else:
            lblA.config(text = "Try again,\nwhat is the colour of the sky?")
       
    #Disables the main menu button
    btnA.config(relief =SUNKEN, state = tk.DISABLED)

    #Makes a new window
    windowA = tk.Toplevel()
    windowA.geometry("400x300")
    windowA.title("Question A")

    #Add components to the window
    lblA = tk.Label(windowA,text = "What colour is the sky?")
    entryA = tk.Entry(windowA)
    submitBtnA = tk.Button(windowA, text = "Submit", command = checkAnswerA)

    lblA.pack()
    entryA.pack()
    submitBtnA.pack()

    windowA.mainloop()

	

#TODO: Add questions B and C

root = tk.Tk()
root.title("Main Menu")

#Set score
score = 0

#Buttons
btnA = tk.Button(text = "Question A", command = questionA)
btnB = tk.Button(text = "Question B") #These do nothing
btnC = tk.Button(text = "Question C")
scoreLbl = tk.Label(text = "Score: "+ str(score))

#Grid set up
btnA.grid(row = 0, column = 0, pady = 2, padx = 2)
btnB.grid(row = 1, column = 0, pady = 2, padx = 2)
btnC.grid(row = 0, column = 1, pady = 2, padx = 2)
scoreLbl.grid(row = 1, column = 1, pady = 2, padx = 2)

"""
Grids work with rows and columns, making it easier to manage how your app looks,
padx and pady will provide pixels in spacing between them and other elements,
ipadx and ipady will space inside the widget making it take up more space.
columnspan will set how wide the element is.
"""


#end of app
root.mainloop()



