# -*- coding: utf-8 -*-
"""
Created on Mon Nov 09 22:39:12 2015

@author: Kevin
"""

class Direction:
        
    
    #funcion de retorno de iteraciones
    def ED(self,x):
        if (x<180.0/2):
            return -2.0/180.0*x+1
        elif (3*180.0/2<x):
            return 2.0/180.0*(x-3*180.0/2)
        return 0
        
    def ND(self,x):
        if (0<=x<180.0/2):
            return 2.0/180.0*x
        elif (180.0/2 <= x < 180.0):
            return -2.0/180.0*(x-180.0)
        return 0
        
    def WD(self,x):
        if (180.0/2<=x<180.0):
            return 2.0/180.0*(x-180.0/2)
        elif (180.0 <= x < 3*180.0/2):
            return -2.0/180.0*(x-3*180.0/2)
        return 0
        
    def SD(self,x):
        if (180.0<=x<3*180.0/2):
            return 2.0/180.0*(x-180.0)
        elif (3*180.0/2 <= x < 2*180.0):
            return -2.0/180.0*(x-2*180.0)
        return 0
     

    