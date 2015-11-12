# -*- coding: utf-8 -*-
"""
Created on Mon Nov 09 23:43:26 2015

@author: Kevin
"""
from Robot import Robot
from Pelota import Pelota
from random import random
from Porteria import Porteria
from Direction import Direction
from Distance import Distance
from Front import Front
import time
from matplotlib.pyplot import plot,draw,show
from math import acos,pi,sin,cos
from pylab import dot,norm,array
import numpy as np

def angle(v1,v2):
    v1 = array(v1)
    v2 = array(v2)
    val = dot(v1,v2)/float(norm(v1)*norm(v2))
    while val<-1:
        val += 2
    
    while val>1:
        val -= 2
        
        
    a = acos(val)
    a = a*180/pi
    return a

def integrate(f,a,b,h = 0.01):
    val = 0
    n = 0
    while n*h+a<=b :
        val += f(n*h+a)*h
        n += 1
        
    return val



class Game:
    
    robot = None
    pelota = None
    porteria = None
    
    #inicializamos juego con pelota y 
    def __init__(self,dimension = [0,0]):#requiere dimension del campo
        rx = dimension[0]*random()#inicializamos posicion x
        ry = dimension[1]*random()#inicializamos posicion y
        self.robot = Robot(pos = [rx,ry])#posicion
        
        self.robot.setAngle(random()*360)#colocamos un angulo aleatorio
        
        px = dimension[0]*random()#posicion x pelota
        py = dimension[1]*random()#posicion y pelota
        self.pelota = Pelota(pos = [px,py])
        
        #colocamos la porteria a la derecha por defecto
        x = dimension[0]#porteria en la derecha
        yini = dimension[1]/2.0-dimension[1]/6.0#se coloca a un tercio de altura
        yfin = dimension[1]/2.0+dimension[1]/6.0#que llegue hasta dos tercios 
        self.porteria = Porteria(init=[x,yini],end=[x,yfin])
        
    
    def action(self):
        direction = self.robot.getAngle()#direction es angulo en el campo del robot
        posicion = self.robot.getVel()#hacia donde apunta 
        posicionP = self.pelota.getPos()-self.robot.getPos()#donde se encuentra la pelota relativo al robot
#        print distance
#        print direction        
        
        fr = Front()
        
#        print "robot: P."+str(self.robot.getPos())+" V."+str(posicion)
#        print "pelota:"+str(self.pelota.getPos())+" PR."+str(posicionP)

        angleb = angle(posicion,[posicionP[0],posicionP[1]])#calculo el angulo entre ellos
#        print "angulo entre ellos:"+str(angleb)
#        print "direction:"+str(direction)
        vectorp = norm(posicionP)*array([cos((direction+angleb)/180.0*pi),-sin((direction+angleb)/180.0*pi)])#supongo que el angulo se mide hacia la izquierda
        #vuelvo a calcular un vector supuesto que tenga la misma direccion
#        print "nuevo:"+str(vectorp)+" compar:"+str(posicionP)
        vectorp = vectorp-posicionP#calculo la diferencia de valores
        if norm(vectorp)>10:
            #quiere decir que esta medido a la derecha
            angleb = -angleb
        
        fr.setTR(fr.TR(angleb))
        fr.setST(fr.ST(angleb))
        fr.setTL(fr.TL(angleb))
        
#        i1 = []
#        for i in range(-90,90,5):
#            i1.append(fr.evalFunc(i))
#            
#        plot([i for i in range(-90,90,5)],i1)
#        show()
#        
#        
        
        val = integrate(lambda x:fr.evalFuncUp(x),-45,45)
        if val!=0:
            val = val/integrate(lambda x:fr.evalFunc(x),-45,45)
            

        print "Cambio de angulo:"+str(val)
        print "Angulo o:"+str(self.robot.getAngle())
        self.robot.addAngle(val)
        self.robot.move()
    
        print "Robot:"+str(self.robot.getPos())
        print "Pelota:"+str(self.pelota.getPos())
        
#        time.sleep(1)
        
    
    def play(self):
        self.action()
        return self.porteria.revisarAdentro(self.pelota.getPos())
        
    def inContact(self):
        return self.pelota.inContact(self.robot.getPos())
    
    def shot(self):
        direction = self.robot.getAngle()#direction es angulo en el campo del robot
        posicion = self.robot.getVel()#hacia donde apunta 
        posicionP = self.porteria.getMed()-self.robot.getPos()#donde se encuentra la pelota relativo al robot
        
        angleb = angle(posicion,[posicionP[0],posicionP[1]])#calculo el angulo entre ellos

        vectorp = norm(posicionP)*array([cos((direction+angleb)/180.0*pi),-sin((direction+angleb)/180.0*pi)])#supongo que el angulo se mide hacia la izquierda
        
        vectorp = vectorp-posicionP#calculo la diferencia de valores
        if norm(vectorp)>10:
            #quiere decir que esta medido a la derecha
            angleb = -angleb
            
        self.robot.addAngle(angleb+self.robot.shotError())
        self.pelota.setVel(3*self.robot.getVel())
        self.pelota.move()
    
    def getRobot(self):
        return self.robot
        
    def getPelota(self):
        return self.pelota
        
    def getPorteria(self):
        return self.porteria

    
    