# -*- coding: utf-8 -*-
"""
Created on Mon Nov 09 23:01:46 2015

@author: Kevin
"""

class Front:
    maxTL = 0.0
    maxST = 0.0
    maxTR = 0.0
    
    #funcion de retorno de iteraciones
    def TL(self,x):
        if (x<-7.5):
            return 1
        elif (-7.5<=x<0):
            return -2.0/15*x
        return 0
        
    def ST(self,x):
        if (x<-7.5):
            return 0
        elif (-7.5<=x<0):
            return 2.0/15*x+1
        elif (0<=x<7.5):
            return -2.0/15*x+1
        return 0
        
    def TR(self,x):
        if (0<x<=7.5):
            return 2.0/15*x
        elif (7.5<x):
            return 1
        return 0
     
    #limitantes de funcion
    def setTL(self,x):
        if (x>self.maxTL):
            self.maxTL = x
            
    def setST(self,x):
        if (x>self.maxST):
            self.maxST = x
            
    def setTR(self,x):
        if (x>self.maxTR):       
            self.maxTR = x
        
    def evalFunc(self,x):
        x1 = self.TL(x)
        if (x1>self.maxTL):
            x1 = self.maxTL
        
        x2 = self.ST(x)
        if (x2>self.maxST):
            x2 = self.maxST
            
        x3 = self.TR(x)
        if (x3>self.maxTR):
            x3 = self.maxTR
        
        return max([x1,x2,x3])