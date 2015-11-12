import Tkinter
import random
import time
import math
import pylab
from Game import Game
from math import pi




        
#param:
#        x = nueva posicion a mover
#        y = nueva posicion a mover
#se mueve de tal forma que tome 1 segundo en llegar a su destino
def MoverJugador():
    rpos = g.getRobot().getPos()
#    print "Pos:"+str(rpos)
    rvel = g.getRobot().getVel()
#    print "Vel:"+str(rvel)
    xpaso = rvel[0]/20.0
#    print "Pasox:"+str(xpaso)
    ypaso = rvel[1]/20.0
#    print "Pasoy:"+str(ypaso)
    for i in range(20):
        
        Cancha.coords(robot,int(rpos[0]-10+i*xpaso),int(rpos[1]-10+i*ypaso),int(rpos[0]+10+i*xpaso),int(rpos[1]+10+i*ypaso))
    
        xy = [int(rpos[0]+i*xpaso), int(rpos[1]+i*ypaso), int(rpos[0]+rvel[0]+i*xpaso), int(rpos[1]+rvel[1]+i*ypaso)]        
        
        Cancha.coords(rdir,*xy)
        Cancha.update()        
        time.sleep(0.005)
        
def Rotar():
    x = Cancha.coords(rdir)#x contiene las coordenadas del palito
    v = g.getRobot().getVel()#v contiene la nueva velocidad
    vo = [x[2]-x[0],x[3]-x[1]]#vo tiene velocidad inicial

    xpaso = (v[0]-vo[0])/10.0
    ypaso = (v[1]-vo[1])/10.0
    
    for i in range(10):
        xy = [x[0], x[1], int(x[2]+i*xpaso), int(x[3]+i*ypaso)]
        Cancha.coords(rdir,*xy)
        Cancha.update()
        time.sleep(0.005)
  
def MoverPelota():
    
    rpos = g.getPelota().getPos()-g.getPelota().getVel()
#    print "Pos:"+str(rpos)
    rvel = g.getPelota().getVel()
#    print "Vel:"+str(rvel)
    xpaso = rvel[0]/20.0
#    print "Pasox:"+str(xpaso)
    ypaso = rvel[1]/20.0
#    print "Pasoy:"+str(ypaso)
    for i in range(20):
        
        Cancha.coords(pelota,int(rpos[0]-10+i*xpaso),int(rpos[1]-10+i*ypaso),int(rpos[0]+10+i*xpaso),int(rpos[1]+10+i*ypaso))
    
        Cancha.update()        
        time.sleep(0.005)


def DibujarCancha(x,y):
    Cancha.create_line(x,y,x-100,y, fill = "white", width = 10)
    Cancha.create_line(x-100,y-5,x-100,y+205, fill = "white", width = 10)
    Cancha.create_line(x,y+200,x-100,y+200, fill = "white", width = 10)
    Cancha.create_line(200,0,200,600, fill = "white", width = 10)
    
    

   



g = Game(dimension=[800,600])
ventana = Tkinter.Tk()
ventana.geometry('800x600')
ventana.title("MiniProyecto 5 Kevin García - 13177; Angel Morales 13332")
ventana.maxsize(width = 800, height = 600)
ventana.minsize(width = 800, height = 600)
Cancha = Tkinter.Canvas(ventana, bg = "green", width = 800, height = 600)
DibujarCancha(800,200)

rpos = g.getRobot().getPos()
robot = Cancha.create_oval(rpos[0]-10, rpos[1]-10, rpos[0]+10, rpos[1]+10, outline='black', fill='gray40', tags=('robot'))

rvel = g.getRobot().getVel()
rdir = Cancha.create_line(rpos[0],rpos[1],rpos[0]+rvel[0],rpos[1]+rvel[1], fill = "white", width = 5,tags='dir')

ppos = g.getPelota().getPos()
pelota = Cancha.create_oval(ppos[0]-10, ppos[1]-10, ppos[0]+10, ppos[1]+10, outline='black', fill='white', tags=('pelota'))
Cancha.pack()

while not g.play():
    MoverJugador()
    g.action()
    Rotar()
    if g.inContact():
        g.shot()
        Rotar()
        MoverPelota()
#    raw_input("Pausa")
    
    

ventana.mainloop()

