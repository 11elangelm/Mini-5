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
from scipy import integrate
import time
from matplotlib.pyplot import plot

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
        distance = self.pelota.getPos()[0]-self.robot.getPos()[0]#distance mide X
        direction = self.robot.getAngle()#direction es angulo en el campo del robot
        print distance
        print direction        
        dr = Direction()
        dx = Distance()
        fr = Front()
        
        #casos 
        fr.setTL(max(dr.ND(direction),dx.RST(distance)))
        fr.setST(max(dr.ND(direction),dx.CT(distance)))
        fr.setTR(max(dr.ND(direction),dx.LST(distance)))
        
        fr.setTL(max(dr.ED(direction),dx.RST(distance)))
        fr.setTL(max(dr.ED(direction),dx.CT(distance)))
        fr.setST(max(dr.ED(direction),dx.LST(distance)))
        
        fr.setTR(max(dr.SD(direction),dx.RST(distance)))
        fr.setTL(max(dr.SD(direction),dx.CT(distance)))
        fr.setTL(max(dr.SD(direction),dx.LST(distance)))
        
        fr.setST(max(dr.WD(direction),dx.RST(distance)))
        fr.setTR(max(dr.WD(direction),dx.CT(distance)))
        fr.setTR(max(dr.WD(direction),dx.LST(distance)))
        #termina casos
        
        i1 = []
        for i in range(-20,20):
            i1.append(fr.evalFunc(i))
            
        plot([i for i in range(-20,20)],i1)
        
        val = integrate.quad(lambda x: fr.evalFunc(x)*x,-20,20)[0]
        
        
        if val != 0:
            val = val/integrate.quad(lambda x: fr.evalFunc(x),-20,20)[0]
        
        self.robot.addAngle(val)
        self.robot.move()
        
        print "Robot:"+str(self.robot.getPos())
        print "Pelota:"+str(self.robot.getVel())
        if self.pelota.inContact(self.robot.getPos()):
            raw_input("ya toco")
        time.sleep(1)
        
    
    def play(self):
        while not self.porteria.revisarAdentro(self.pelota.getPos()):
            self.action()#seguir jugando
        
        
    
    
    def getRobot(self):
        return self.robot
        
    def getPelota(self):
        return self.pelota
        
    def getPorteria(self):
        return self.porteria

    
    