# -*- coding: utf-8 -*-
"""
Created on Mon Nov 09 17:41:38 2015

@author: Kevin
"""
from pylab import array
from math import  pi, cos, sin
import numpy as np

#un robot tiene posicion (x,y) y velocidad (x,y)
class Robot:
    posicion = array([])#posicion x,y
    velocidad = array([])#velocidad vector x,y
    angulo = 0.0#angulo 0<theta<306
    rangulo = 0.0#angulo "real"
    longitud = 10.0#longitud absoluta de movimiento
    error = 10.0
    
        
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
        
    def setAngle(self,angle):
        #suponemos que el angulo es en grados y 0<theta<360
        
        self.velocidad = self.longitud*array([cos(angle/180.0*pi),-sin(angle/180.0*pi)])
        self.angulo = angle
        self.rangulo = angle
        
    #funcion de retorno de raiz
    def setVel(self,vel):
        self.velocidad = array(vel)
        
    def move(self):
        self.posicion = self.posicion+self.velocidad
        
    def getAngle(self):
        return self.angulo
        
    def addAngle(self,angle):
        tangulo = self.rangulo+angle#solo le sumamos el angulo
        self.setAngle((self.angulo+angle)%360)#calculamos su relativo en 360°
        self.rangulo = tangulo#remplazamos el valor de rangulo
        
    def getOrAng(self):
        return self.rangulo
        
    def shotError(self):
        return np.random.normal(0,self.error,1)