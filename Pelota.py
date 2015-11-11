# -*- coding: utf-8 -*-
"""
Created on Mon Nov 09 18:02:07 2015

@author: Kevin
"""

from pylab import array
from math import sqrt

#un robot tiene posicion (x,y) y velocidad (x,y)
class Pelota:
    posicion = array([])#posicion x,y
    direccion  = array([])#velocidad vector x,y
    radio = 10.0#radio para verificar si ha tocado
        
    def __init__(self,pos = [0,0], vel = [0,0]):
        self.posicion = array(pos)
        self.velocidad = array(vel)
    #funcion de retorno de iteraciones
    def getPos(self):
        return self.posicion
        
    def getVel(self):
        return self.velocidad
    
    #funcion de retorno de convergencia
    def setPos(self, pos):
        self.posicion = array(pos)
        
    #funcion de retorno de raiz
    def setVel(self,vel):
        self.velocidad = array(vel)
        
    def move(self):
        self.posicion = self.posicion+self.velocidad
    
    def getRadio(self):
        return self.radio
        
    def setRadio(self,radio):
        self.radio = radio
        
    def inContact(self,pos):
        #pos = [x,y] del jugador
        val = sqrt((pos[0]-self.posicion[0])**2+(pos[1]-self.posicion[1])**2)
        if val <= self.radio:
            return True
        return False