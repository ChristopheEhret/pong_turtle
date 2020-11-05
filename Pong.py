# -*- coding: utf-8 -*-
"""
Created on Sat Oct 14 23:23:27 2017

@author: Christophe
"""

import turtle as tr
import time
import random as rng

posJ1 = [-360, 75]
vitesseJ1 = 0

posJ2 = [340, 75]
vitesseJ2 = 0
chanceIA = 100

tailleBarre = [20, 150]

posBalle = [-10, -10]
coteBalle = 20
vitesseBaseBalle = 5
vitesseXBalle = -5
vitesseYBalle = -5

jeu = True

def dessineRectangle(x, y, largeur, hauteur):    
    tr.setheading(0)
    tr.up()
    
    tr.goto(x, y)
    tr.down()
    
    for i in range(4):
        if(i == 0 or i == 2):
            tr.fd(largeur)
        else:
            tr.fd(hauteur)
        tr.rt(90)
        
def reset():
    global posJ1
    global vitesseJ1
    global posJ2
    global vitesseJ2
    global arriveeIAJ2
    global posBalle
    global vitesseXBalle
    global vitesseYBalle
    global vitesseBaseBalle
    
    posJ1 = [-360, 75]
    vitesseJ1 = 0
    
    posJ2 = [340, 75]
    vitesseJ2 = 0
    arriveeIAJ2 = [340, 75]
    
    posBalle = [-10, 10]
    vitesseXBalle = -5
    vitesseYBalle = -5
    vitesseBaseBalle = 5
        
def dessin():
    tr.clear()
    dessineRectangle(posJ1[0], posJ1[1], tailleBarre[0], tailleBarre[1])
    dessineRectangle(posJ2[0], posJ2[1], tailleBarre[0], tailleBarre[1])
    dessineRectangle(posBalle[0], posBalle[1], coteBalle, coteBalle)
    dessineRectangle(-400, -300, 800, 50)
    dessineRectangle(-400, 350, 800, 50)
    tr.update()  
    
def checkCollision(x1, y1, l1, h1, x2, y2, l2, h2):
    return ((x1 <= x2 + l2 and x1 + l1 >= x2) and (y1 >= y2 - h2 and y1 - h1 <= y2))

def manageIA():
    global vitesseJ2
    global vitesseBaseBalle
    global chanceIA
    
    vitesseJ2 = 0
        
    if(posBalle[1] >= posJ2[1] - (tailleBarre[1]/2) + 30):
        if(rng.randint(0, 80) <= chanceIA):
            vitesseJ2 = vitesseBaseBalle
    elif(posBalle[1] - coteBalle <= posJ2[1] - (tailleBarre[1]/2) - 30):
        if(rng.randint(0, 80) <= chanceIA):
            vitesseJ2 = -vitesseBaseBalle
            
def tick():
    global vitesseYBalle
    global vitesseXBalle
    global vitesseBaseBalle
    global posBalle
    global posJ1
    global vitesseJ1
    global posJ2
    global vitesseJ2
    global chanceIA
    
    oldPosBalleX = posBalle[0]
    posBalle[0] += vitesseXBalle
    
    if(checkCollision(posBalle[0], posBalle[1], coteBalle, coteBalle, posJ1[0], posJ1[1], tailleBarre[0], tailleBarre[1]) or checkCollision(posBalle[0], posBalle[1], coteBalle, coteBalle, posJ2[0], posJ2[1], tailleBarre[0], tailleBarre[1])):
        if(vitesseXBalle > 0):
            vitesseXBalle = -1 * vitesseBaseBalle
        else:
            vitesseXBalle = vitesseBaseBalle   
             
        #vitesseBaseBalle += 0.1
        posBalle[0] = oldPosBalleX  
        
        chanceIA -= 1
    elif(posBalle[0] <= -343 or posBalle[0] + coteBalle >= 343):
        reset()
    
    
    oldPosBalleY = posBalle[1]
    posBalle[1] += vitesseYBalle
    
    if(checkCollision(posBalle[0], posBalle[1], coteBalle, coteBalle, posJ1[0], posJ1[1], tailleBarre[0], tailleBarre[1]) or checkCollision(posBalle[0], posBalle[1], coteBalle, coteBalle, posJ2[0], posJ2[1], tailleBarre[0], tailleBarre[1])):
        if(vitesseYBalle > 0):
            vitesseYBalle = -1 * vitesseBaseBalle
        else:
            vitesseYBalle = vitesseBaseBalle
             
        #vitesseBaseBalle += 0.1
        posBalle[1] = oldPosBalleY
        
    elif(posBalle[1] - coteBalle <= -300 or posBalle[1] >= 300):
        if(vitesseYBalle > 0):
            vitesseYBalle = -1 * vitesseBaseBalle
        else:
            vitesseYBalle = vitesseBaseBalle
             
        #vitesseBaseBalle += 0.1
        posBalle[1] = oldPosBalleY
        
    manageIA()
    
    oldPosJ1 = posJ1[1]
    posJ1[1] += vitesseJ1 
    
    if(posJ1[1] >= 300 or posJ1[1] - tailleBarre[1] <= -300):
        posJ1[1] = oldPosJ1
        
    oldPosJ2 = posJ2[1]
    posJ2[1] += vitesseJ2
    
    if(posJ2[1] >= 300 or posJ2[1] - tailleBarre[1] <= -300):
        posJ2[1] = oldPosJ2
    
    
def allerHaut():
    global vitesseJ1
    if(vitesseJ1 == 5):
        vitesseJ1 = 0
    else:
        vitesseJ1 = 5
        
def allerBas():
    global vitesseJ1
    if(vitesseJ1 == -5):
        vitesseJ1 = 0
    else:
        vitesseJ1 = -5
 
def main():

    tr.title("Pong !")     
    tr.speed(0)
    tr.ht()
    tr.tracer(0 ,0)
    
    tr.onkey(allerHaut, "Up")
    tr.onkey(allerBas, "Down")
    
    timer = 0
    while(jeu):
        timer += 1
        time.sleep(0.01)
        if(timer >= 16):
            tr.listen()
            tick()
            dessin()

    
    tr.done()