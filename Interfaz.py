import Tkinter
import random
import time
import math
import pylab

r = 30

bx = random.uniform(5,795)
by = random.uniform(5,595)
rx = random.uniform(5,795)
ry = random.uniform(5,595)
a = random.uniform(0,2*math.pi)
ganar = False
"""def MoverPelota(x,y):
#    jx = jx + 10*math.cos(a)
#    jy = jy + 10*math.sin(a)
#    j.delete("all")
#    j.pack()
#    coord = 25,25,(25+25*math.cos(a)),(25+25*math.sin(a))
#    j.create_line(coord, width=4, fill="red")
#    j.place(x = jx, y = jy)
#    form.update()
#    time.sleep(0.1)
    Cancha.create_oval(x-5,y-5,x+5,y+5, fill = "white", outline = "white")
    Cancha.pack()"""
    
def RotarRobot(a,anew,x,y):
    for i in pylab.linspace(a,anew,10):
#    for i in linspace(a,anew,1):
        print i
        MoverRobot(x,y,i*math.pi/180)
#        time.sleep(1)
        Cancha.pack()
        ventana.update()
    
def MoverRobot(x,y,a):
#    a = a / 180*pi
#    Cancha.create_polygon(rx,ry,rx+rx*cos(ang),(ry-5)-ry*sin(ang),rx+(rx+10)*cos(ang),ry+(ry+15)*sin(ang),rx+rx*cos(ang),ry+(ry+5)*sin(ang),rx-(rx-10)*cos(ang),ry+(ry+15)*sin(ang),rx+rx*cos(ang),(ry-5)-ry*sin(ang), width = 10, fill = "red")
#    Cancha.create_polygon(rx,ry,rx+rx*cos(ang)-ry*sin(ang),(ry-5)-ry*sin(ang),rx+(rx+10)*cos(ang)-ry*sin(ang),ry+(ry+15)*sin(ang),rx+rx*cos(ang)-ry*sin(ang),ry+(ry+5)*sin(ang),rx-(rx-10)*cos(ang)-ry*sin(ang),ry+(ry+15)*sin(ang),rx+rx*cos(ang)-ry*sin(ang),(ry-5)-ry*sin(ang), width = 10, fill = "red")
#    Cancha.create_polygon(rx,ry,rx*cos(ang)-(ry-5)*sin(ang),(ry-5)*sin(ang)+rx*cos(ang),rx+(rx+10)*cos(ang)-ry*sin(ang),ry+(ry+15)*sin(ang)+rx*cos(ang),rx+rx*cos(ang)-ry*sin(ang),ry+(ry+5)*sin(ang)+rx*cos(ang),rx-(rx-10)*cos(ang)-ry*sin(ang),ry+(ry+15)*sin(ang)+rx*cos(ang),rx+rx*cos(ang)-ry*sin(ang),(ry-5)-ry*sin(ang)+rx*cos(ang), width = 10, fill = "red")
    Cancha.create_polygon(x+10,y+15,x,y+5,x-10,y+15,x,y-5, width = 10, fill = "blue")
#    Cancha.create_polygon(x*cos(a)-(y-5)*sin(a),x*sin(a)+(y-5)*cos(a),(x+10)*cos(a)-(y+15)*sin(a),(x+10)*sin(a)+(y+15)*cos(a),x*cos(a)-(y+5)*sin(a),x*sin(a)+(y+5)*cos(a),(x-10)*cos(a)-(y+15)*sin(a),(x-10)*sin(a)+(y+15)*cos(a),x*cos(a)-(y-5)*sin(a),x*sin(a)+(y-5)*cos(a),width = 10, fill = "red")
#    parriba = x*cos(a)-(y-5)*sin(a),x*sin(a)+(y-5)*cos(a)
#    pderecha =(x+10)*cos(a)-(y+15)*sin(a),(x+10)*sin(a)+(y+15)*cos(a)
#    pmedio = x*cos(a)-(y+5)*sin(a),x*sin(a)+(y+5)*cos(a)
#    pizquierda = (x-10)*cos(a)-(y+15)*sin(a),(x-10)*sin(a)+(y+15)*cos(a)
#    parriba = x*cos(a)-(y-5)*sin(a),x*sin(a)+(y-5)*cos(a)
#    pderecha =(x+10)*cos(a)-(y+15)*sin(a),(x+10)*sin(a)+(y+15)*cos(a)
#    pmedio = x*cos(a)-(y+5)*sin(a),x*sin(a)+(y+5)*cos(a)
#    pizquierda = (x-10)*cos(a)-(y+15)*sin(a),(x-10)*sin(a)+(y+15)*cos(a)
    Cancha.create_polygon(parriba,pderecha,pmedio,pizquierda,fill="red")
#    Cancha.create_polygon(x*cos(a)-(y-5)*sin(a),x*sin(a)+(y-5)*cos(a),(x+10)*cos(a)-(y+15)*sin(a),(x+10)*sin(a)+(y+15)*cos(a),x*cos(a)-(y+5)*sin(a),x*sin(a)+(y+5)*cos(a),(x-10)*cos(a)-(y+15)*sin(a),(x-10)*sin(a)+(y+15)*cos(a),x*cos(a)-(y-5)*sin(a),x*sin(a)+(y-5)*cos(a),width = 10, fill = "red")
    Cancha.pack()
    
def RotarPalito(a,anew,x,y):
    for i in pylab.linspace(a,anew,360):
        Cancha.delete("all")
        MoverPalito(x,y,i)
#        MoverPelota(bx,by)
        DibujarCancha(800,200)
        time.sleep(0.001)
        ventana.update()
        Cancha.pack()
        
def MoverPalito(x,y,a):
#    Cancha.create_line(x,y,x+5,y, width = 4, fill = "blue")
    r = 30
    Cancha.create_line(x,y,x+r*math.cos(a),y+r*math.sin(a), fill = "white", width = 5)
    Cancha.create_oval(x-3,y-3,x+3,y+3, fill = "red", width = 1)
    Cancha.pack()
    
def MoverPelota(x1,y1,x2,y2):
    tam = ((y2-y1)**2 + (x2-x1)**2)**0.5
    tf = random.uniform(0,tam)
#    xcam = pylab.linspace(x1,x1+tf,tam)
#    ycam = pylab.linspace(y1,y1+tf,tam)
    xcam = pylab.linspace(x1,x2,tam)
    ycam = pylab.linspace(y1,y2,tam)
    print ycam
    Cancha.create_oval(x1-5,y1-5,x1+5,y1+5, fill = "white", outline = "white")
    for i in range(len(xcam)):
        Cancha.delete("all")
        Cancha.create_oval(xcam[i]-5,ycam[i]-5,xcam[i]+5,ycam[i]+5, fill = "white", outline = "white")
        DibujarCancha(800,200)
        MoverPalito(rx,ry,a)
        Cancha.pack()
        ventana.update()
        time.sleep(0.001)
        
def MoverJugador(x1,y1,x2,y2):
    tam = ((y2-y1)**2 + (x2-x1)**2)**0.5
    xcam = pylab.linspace(x1,x2,tam)
    ycam = pylab.linspace(y1,y2,tam)
    for i in range(len(xcam)):
        Cancha.delete("all")
        MoverPelota(bx,by,bx,by)
        MoverPalito(xcam[i],ycam[i],a)
        DibujarCancha(800,200)
        Cancha.pack()
        ventana.update()
        time.sleep(0.001)
    
        
    
    
"""def MoverPalito(x1,y1,x2,y2):
    Cancha.create_line(x1,y1,x2,y2, fill = "white", width = 5)
    Cancha.create_oval(x1-3,y1-3,x1+3,y1+3, fill = "red", width = 1)
    Cancha.pack()"""

def DibujarCancha(x,y):
    Cancha.create_line(x,y,x-100,y, fill = "white", width = 10)
    Cancha.create_line(x-100,y-5,x-100,y+205, fill = "white", width = 10)
    Cancha.create_line(x,y+200,x-100,y+200, fill = "white", width = 10)
    Cancha.create_line(200,0,200,600, fill = "white", width = 10)
    Cancha.pack()

def AnguloPalitoPelota():
    angulo = math.atan2((by-ry),(bx-rx))
    print angulo
    return angulo
    
def AnguloPelotaPorteria(x,y):
    angulo = math.atan2((y-by),(x-bx))
    return angulo

def ObtenerCamino(rx,ry,bx,by):
    cx = []
    cy = []
    ang = AnguloPalitoPelota()
    while (rx != bx) and (ry != by):
        angulo = random.random()
#        print angulo
        if (angulo <= 0.1):
            uni = random.uniform(math.pi+ang,math.pi*2+ang)
        elif (angulo <= 0.3):
            uni = random.uniform(0+ang,math.pi/9+ang)
        elif (angulo <= 0.8):
            uni = random.uniform(math.pi/9+ang,math.pi*18/11+ang)
        elif (angulo <= 1):
            uni = random.uniform(math.pi*18/11+ang,math.pi*2+ang)
        rx = rx + math.cos(uni)
        ry = ry + math.sin(uni)
        cx.append(rx)
        cy.append(ry)
        print rx,ry,bx,by,
#    print cx,cy
    return cx,cy
    
ventana = Tkinter.Tk()
ventana.geometry('800x600')
ventana.title("MiniProyecto 5 Kevin García - 13177; Angel Morales 13332")
ventana.maxsize(width = 800, height = 600)
ventana.minsize(width = 800, height = 600)
Cancha = Tkinter.Canvas(ventana, bg = "green", width = 800, height = 600)
RotarPalito(a,AnguloPalitoPelota(),rx,ry)
a = AnguloPalitoPelota() 
MoverJugador(rx,ry,bx,by)

rx = bx
ry = by
RotarPalito(a,AnguloPelotaPorteria(800,300),rx,ry)
a = AnguloPelotaPorteria(800,300)
MoverPelota(bx,by,800,300)
Cancha.pack()

ventana.mainloop()
#MoverPalito(rx,ry,a)
#for i in range(int(rx),int(bx)):
#    print i
#    MoverRobot(i,ry)
#    ventana.update()
#    time.sleep(0.1)
#Cancha.create_oval(bx-5,by-5,bx+5,by+5, width = 10, fill = "white", outline = "white")
#pelota = Cancha.create(bx-5,by-5,bx+5,by+5, width = 10, fill = "white", outline = "white")
#MoverRobot(rx,ry,0)
#MoverRobot(rx,ry,pi/12)
#MoverRobot(rx,ry,pi/9)
#MoverRobot(rx,ry,pi/6)
#MoverRobot(rx,ry,pi/3)
#MoverRobot(rx,ry,pi/2)
#MoverRobot(rx,ry,pi)
#RotarRobot(0,30,600,0)
#MoverRobot(rx,ry,3*pi/2)
#MoverPalito(100,100,pi/2)
#MoverPalito(rx,ry,AnguloPalitoPelota())
#for i in pylab.linspace(rx,bx,50):
#    Cancha.delete("all")
#    MoverPalito(i,ry,AnguloPalitoPelota())
#    MoverPelota(bx,by)
#    DibujarCancha(800,200)
#    time.sleep(0.1)
#    ventana.update()
#print a, AnguloPalitoPelota()
#while not ganar:
#RotarPalito(a,AnguloPalitoPelota(),rx,ry)
#camino = ObtenerCamino(rx,ry,bx,by)
#Patear()
#    for item in camino[0]: 
#        MoverPalito()
#    camino = ObtenerDireccion(rx,ry,bx,by)
#MoverRobot(rx,ry,pi/8   )
#robot = Cancha.create_polygon(rx,ry-5,rx+10,ry+15,rx,ry+5,rx-10,ry+15, width = 10, fill = "red")

# Dibujar puntito y rotar 
# MoverPelota cuando pega
