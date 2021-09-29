from tkinter import *
import random
from pyttsx3 import speak as sp
from PIL import ImageTk,Image
##Creation of objects
root=Tk()
#Geometry
root.geometry("500x500")
root.title("Rock Paper Scissor Game")

##Computer value
computer_value={ "0":"Rock","1":"Paper","2":"Scissor"}





##Reset the game

def reset_game():
    b1['state']="normal"
    b2['state']="normal"
    b3['state']="normal"
    l1.config(text="Player")
    l3.config(text="Computer")
    l4.config(text= "")
    
##Disable the button
def button_disable():
    b1['state']="disable"
    b2['state']="disable"
    b3['state']="disable"
    
##If player selected rock
def isrock():
    c_v= computer_value[str(random.randint(0,2))]
    if c_v=="Rock":
        match_result="Match Draw"
        sp("Match Draw")
    elif c_v=="Scissor":
        match_result="Match Won"
        sp("Match Won")
    else :
        match_result="Match Lose !! Computer has won"
        sp("Match losed")
    l4.config(text=match_result)
    l1.config(text="Rock")
    l3.config(text=c_v)
    button_disable()
        
##If a player selected paper  

def ispaper():
    c_v= computer_value[str(random.randint(0,2))]
    if c_v=="Paper":
        match_result="Match Draw"
        sp("Match Draw")
    elif c_v=="Scissor":
        match_result="Match lose !! Computer has Won "
        sp("Match Losed")
    else :
        match_result="Match Won"
        sp("Match Won")
    l4.config(text=match_result)
    l1.config(text="Paper")
    l3.config(text=c_v)
    button_disable()
    
## if a plater selected scissor

def isscissor():
    c_v= computer_value[str(random.randint(0,2))]
    if c_v=="Rock":
        match_result="Match Lose !! Computer has won"
        sp("Match Losed")
    elif c_v=="Scissor":
        match_result="Match Draw"
        sp("Match Draw")
    else :
        match_result="Match Won"
        sp("Match Won")
    l4.config(text=match_result)
    l1.config(text="Scissor")
    l3.config(text=c_v)
    button_disable()

    ##labels,frames and buttons
Label(root,text="Rock Paper Scissor",font="Arial 40 bold",fg="blue").pack(pady=20)

frame=Frame(root)
frame.pack()

l1=Label(frame,text="Player",font="Arial 30 bold")
l2=Label(frame,text="VS", font="Arial 30 bold")
l3=Label(frame,text="Computer",font="Arial 30 bold")

l1.pack(side=LEFT)
l2.pack(side= LEFT)
l3.pack()

l4=Label(root,text="",font="Arial 20 bold",bg="black",fg="blue",width=15,borderwidth=2,relief="solid")
l4.pack(pady=20,ipadx=100,ipady=40)

frame1=Frame(root)
frame1.pack()
b1=Button(frame1,text="Paper",font=10,width=7,bg="blue",fg="white",command=ispaper)
b2=Button(frame1,text="Rock",font=10,width=7,bg="brown",fg="white",command=isrock)
b3=Button(frame1,text="Scissor",font=10,width=7,bg="silver",fg="white",command=isscissor)

b1.pack(side=LEFT,padx=10,ipadx=30)
b2.pack(side=LEFT,padx=10,ipadx=30)
b3.pack(padx=10,ipadx=30)

Button(root,text="Reset Game",font=10,fg="red",bg='black',command=reset_game).pack(ipadx=30,pady=50)


    

##Execute the looop
root.mainloop()