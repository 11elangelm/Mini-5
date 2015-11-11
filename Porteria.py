# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 02:33:58 2015

@author: Kevin
"""

from pylab import array

class Porteria:
    xyini = None
    xyfin = None
    xmed = None
    
    def __init__ (self, init = array([0,0]), end = array([0,0])):#init posee un valor mas pequeño que end ej: init = [3,4] , end = [3,7]
        self.xyfin = array(end)
        self.xyini = array(init)
        self.xmed = array([(self.xyini[0]+self.xyfin[0])/2.0, (self.xyini[1]+self.xyfin[1])/2.0])
        
    #esta funcion revisa si se acaba el juego segun la posicion de la pelota
    def revisarAdentro(self,pos):
        #pos = [x,y] de la pelota
        if self.xyini[0]==self.xyfin[0]:#quiere decir que es porteria vertical
            if self.xyini[0]>0:#quiere decir que esta del lado derecho
                if (pos[0]>=self.xyini[0]) and (self.xyini[1]<=pos[1]<=self.xyfin[1]):#si esta adentro
                    return True
            else:#quiere decir que esta del lado izquierdo
                if (pos[0]<=self.xyini[0]) and (self.xyini[1]<=pos[1]<=self.xyfin[1]):#si esta adentro
                    return True
        else:#quiere decir que es horizontal
            if self.xyini[1]>0:#quiere decir que esta abajo
                if (pos[1]>=self.xyini[1]) and (self.xyini[0]<=pos[0]<=self.xyfin[0]):#si esta adentro
                    return True
            else:#quiere decir que esta arriba
                if (pos[1]<=self.xyini[1]) and (self.xyini[0]<=pos[0]<=self.xyfin[0]):#si esta adentro
                    return True
        return False
        
    #posicion a apuntar
    def getMed(self):
        return self.xmed
            