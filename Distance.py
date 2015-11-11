# -*- coding: utf-8 -*-
"""
Created on Mon Nov 09 22:10:41 2015

@author: Kevin
"""

class Distance:
    
    
    #funcion de retorno de iteraciones
    def LST(self,x):
        if (x<-7.5):
            return 1
        elif (-7.5<=x<0):
            return -2.0/15*x
        return 0
        
    def CT(self,x):
        if (x<-7.5):
            return 0
        elif (-7.5<=x<0):
            return 2.0/15*x+1
        elif (0<=x<7.5):
            return -2.0/15*x+1
        return 0
        
    def RST(self,x):
        if (0<x<=7.5):
            return 2.0/15*x
        elif (7.5<x):
            return 1
        return 0
