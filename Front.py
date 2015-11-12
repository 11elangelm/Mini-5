# -*- coding: utf-8 -*-
"""
Created on Mon Nov 09 23:01:46 2015

@author: Kevin
"""

class Front:
    maxTL = 0.0
    maxST = 0.0
    maxTR = 0.0
    
    
    def TR(self,x):
        if (x<-90):
            return 1
        elif (-90<=x<-30):
            return -1.0/30*(x+30)
        return 0
        
    def ST(self,x):
        if (x<-45):
            return 0
        elif (-45<=x<0):
            return 1.0/45*(x+45)
        elif (0<=x<45):
            return -1.0/45*(x+45)
        return 0
        
    def TL(self,x):
        if (30<x<=90):
            return 1.0/30*(x-30)
        elif (90<x):
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
        
    def evalFuncUp(self,x):
        x1 = self.TL(x)
        if (x1>self.maxTL):
            x1 = self.maxTL
        
        x2 = self.ST(x)
        if (x2>self.maxST):
            x2 = self.maxST
            
        x3 = self.TR(x)
        if (x3>self.maxTR):
            x3 = self.maxTR
        
        return max([x1,x2,x3])*x