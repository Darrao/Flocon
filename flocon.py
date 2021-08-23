from tkinter import *

joe=turtle.Pen()
tabCouleurs=["red","blue","turquoise","purple","green"]

joe.speed(0)


def motif_flocon(longueur,complexite): 
    if complexite == 0: 
        joe.down() 
        joe.forward(longueur)
        joe.penup() 
    else :
        joe.down() 
        motif_flocon(longueur//3, complexite-1) 
        joe.left(60) 
        motif_flocon(longueur//3, complexite-1) 
        joe.right(120) 
        motif_flocon(longueur//3, complexite-1) 
        joe.left(60) 
        motif_flocon(longueur//3, complexite-1) 
        joe.penup() 





y =0


for i in range(4): 
    joe.goto(0,y) 
    joe.color(tabCouleurs[i%len(tabCouleurs)]) 
    motif_flocon(300,i) 
    y -= 100  
import turtle as tu
tu.speed(0)

def floc(l):
    if l<3:
        tu.fd(l)
        return
    floc(l / 3)
    tu.lt(60)
    floc(l / 3)
    tu.rt(120)
    floc(l / 3)
    tu.lt(60)
    floc(l / 3)

def flocon(l):
    tu.speed(0)
    tu.color('#0000ff', '#55ffff')
    tu.begin_fill()
    for i in range(3):
        floc(l)
        tu.rt(120)
    tu.end_fill()

flocon(100)