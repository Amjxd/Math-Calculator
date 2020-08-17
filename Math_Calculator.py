#Create a calculator app that can add / clear

from tkinter import *
#Window
root = Tk()
root.title("Basic Calculator")
root.configure(background='pink')
root.resizable(width=False,height=False)

#Input box
e = Entry(root,width=35,borderwidth=4,bg='pink',fg='white')
e.grid(column=0,row=0,columnspan = 3) #column span is what keeps the buttons in place


def display_nums(num):
    current = e.get() #get what is in the entry box
    e.delete(0,END)# DELETE EVERYTHING IN THE INPUT BOX
    e.insert(0, str(current) + str(num))  #concatinate what's in the entry box with the number clicked
    
def clear():
    e.delete(0,END)

def add():
    global math
    math = "add"
    current = float(e.get())
    e.delete(0,END)
    global total #Since it is global, we can use it outside this function
    total = current

def subtract():
    global math
    math = "sub"
    current = float(e.get())
    e.delete(0,END)
    global total #Since it is global, we can use it outside this function
    total = current

def multiply():
    global math
    math = "mul"
    current = float(e.get())
    e.delete(0,END)
    global total
    total = current

def divide():
    global math
    math = "div"
    current = float(e.get())
    e.delete(0,END)
    global total
    total = current
    
def equal():
    current2 = float(e.get())
    e.delete(0,END)
    if math == "add":
        final = total + current2
    if math == "sub":
        final = total - current2
    if math == "mul":
        final = total * current2
    if math == "div":
        final = total / current2
    e.insert(0,final)

        
    
#Buttons
#ROW 1
seven = Button(root,width=6,height=2, text = "7", font = ('arial',15, 'bold'), highlightbackground="pink",command =lambda: display_nums(7)).grid(column = 0, row = 1)
eight = Button(root, width=6,height=2,text = "8", font = ('arial',15, 'bold'), highlightbackground="pink",command =lambda: display_nums(8)).grid(column = 1, row = 1)
nine = Button(root,width=6,height=2, text = "9", font = ('arial',15, 'bold'), highlightbackground="pink",command =lambda: display_nums(9)).grid(column = 2, row = 1)
#ROW 2
four = Button(root,width=6,height=2, text = "4", font = ('arial',15, 'bold'), highlightbackground="pink",command =lambda: display_nums(4)).grid(column = 0, row = 2)
five= Button(root,width=6,height=2, text = "5", font = ('arial',15, 'bold'), highlightbackground="pink",command =lambda: display_nums(5)).grid(column = 1, row = 2)
six = Button(root,width=6,height=2, text = "6", font = ('arial',15, 'bold'), highlightbackground="pink",command =lambda: display_nums(6)).grid(column = 2, row = 2)
#ROW 3
one = Button(root,width=6,height=2, text = "1", font = ('arial',15, 'bold'), highlightbackground="pink",command =lambda: display_nums(1)).grid(column = 0, row = 3)
two = Button(root,width=6,height=2, text = "2", font = ('arial',15, 'bold'), highlightbackground="pink",command =lambda: display_nums(2)).grid(column = 1, row = 3)
three = Button(root,width=6,height=2, text = "3", font = ('arial',15, 'bold'), highlightbackground="pink",command =lambda: display_nums(3)).grid(column = 2, row = 3)
#ROW 4
zero = Button(root,width=6,height=2, text = "0", font = ('arial',15, 'bold'), highlightbackground="pink",command =lambda: display_nums(0)).grid(column = 0, row = 4)
#CLEAR
clear = Button(root,width=18,height=2, text = "CLEAR", font = ('arial',15, 'bold'), highlightbackground="pink",command =clear).grid(column = 1, row = 4,columnspan=2)
#ROW 5
#PLUS
plus = Button(root,width=6,height=2, text = "+", font = ('arial',15, 'bold'), highlightbackground="pink",command =add).grid(column = 0, row = 5)
#EQUALS
equals = Button(root,width=18,height=2, text = "=", font = ('arial',15, 'bold'), highlightbackground="pink",command =equal).grid(column = 1, row = 5,columnspan=2)
#ROW 6
divide = Button(root,width=6,height=2, text = "÷", font = ('arial',15, 'bold'), highlightbackground="pink",command =divide).grid(column = 2, row = 6)
multiply = Button(root,width=6,height=2, text = "×", font = ('arial',15, 'bold'), highlightbackground="pink",command =multiply).grid(column = 1, row = 6)
subtract = Button(root,width=6,height=2, text = "-", font = ('arial',15, 'bold'), highlightbackground="pink",command =subtract).grid(column = 0, row = 6)


root.mainloop()
