# Program to show a digital clock
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from sys import argv
from math import radians, cos, sin, tan
from datetime import datetime

def translate(num, factor):
    for i in num:
        for j  in i:
            j[0] += factor
    return num

# time settings
H0 = 0
H1 = 0
M0 = 0
M1 = 0
S0 = 0
S1 = 0

# Digital clock segments
C1 = [-650, 100]
C2 = [-650, -100]
C3 = [250, 100]
C4 = [250, -100]

class digit:
    def __init__(self,args):
        self.a = args[0]
        self.b = args[1]
        self.c = args[2]
        self.d = args[3]
        self.e = args[4]
        self.f = args[5]
        self.g = args[6]

    def getSeg(self, number):
        a = self.a
        b = self.b
        c = self.c
        d = self.d
        e = self.e
        f = self.f
        g = self.g
        if number == 0:
            return [a,b,e,f,g,d]
        elif number == 1:
            return [b,e]
        elif number == 2:
            return [a,b,c,g,f]
        elif number == 3:
            return [a,b,c,e,f]
        elif number == 4:
            return [d,c,b,e]
        elif number == 5:
            return [a,d,c,e,f]
        elif number == 6:
            return [a,d,c,e,f,g]
        elif number == 7:
            return [a,b,e]
        elif number == 8:
            return [a,b,c,d,e,f,g]
        elif number == 9:
            return [a,b,c,d,e]
        else :
            return [a,b,e,f,g,d]
    

HZ = digit(translate([
    [[-1200,300],[-1000,300]],
    [[-950,250],[-950,20]],
    [[-1200,0],[-1000,0]],
    [[-1250,250],[-1250,20]],
    [[-950,-250],[-950,-20]],
    [[-1200,-300],[-1000,-300]],
    [[-1250,-250],[-1250,-20]]
    ],-200))
HO = digit(translate([
    [[-1200,300],[-1000,300]],
    [[-950,250],[-950,20]],
    [[-1200,0],[-1000,0]],
    [[-1250,250],[-1250,20]],
    [[-950,-250],[-950,-20]],
    [[-1200,-300],[-1000,-300]],
    [[-1250,-250],[-1250,-20]]
    ],200))


MZ = digit(translate([
    [[-1200,300],[-1000,300]],
    [[-950,250],[-950,20]],
    [[-1200,0],[-1000,0]],
    [[-1250,250],[-1250,20]],
    [[-950,-250],[-950,-20]],
    [[-1200,-300],[-1000,-300]],
    [[-1250,-250],[-1250,-20]]
    ],700))
MO = digit(translate([
    [[-1200,300],[-1000,300]],
    [[-950,250],[-950,20]],
    [[-1200,0],[-1000,0]],
    [[-1250,250],[-1250,20]],
    [[-950,-250],[-950,-20]],
    [[-1200,-300],[-1000,-300]],
    [[-1250,-250],[-1250,-20]]
    ],1100))

SZ = digit(translate([
    [[-1200,300],[-1000,300]],
    [[-950,250],[-950,20]],
    [[-1200,0],[-1000,0]],
    [[-1250,250],[-1250,20]],
    [[-950,-250],[-950,-20]],
    [[-1200,-300],[-1000,-300]],
    [[-1250,-250],[-1250,-20]]
    ],1700))
SO = digit(translate([
    [[-1200,300],[-1000,300]],
    [[-950,250],[-950,20]],
    [[-1200,0],[-1000,0]],
    [[-1250,250],[-1250,20]],
    [[-950,-250],[-950,-20]],
    [[-1200,-300],[-1000,-300]],
    [[-1250,-250],[-1250,-20]]
    ],2100))


def init():
    glClearColor(1.0,1.0,1.0,1.0)
    gluOrtho2D(-1500,1500,-1500,1500)

def Sign(a):
    if a  > 0 :
        return 1
    if a  < 0 :
        return -1
    if a  == 0:
        return 0

def line(A,B):
    pts = []
    if A == B:
        exit()
    x = A[0]
    y = A[1]
    dx = abs(B[0]-A[0])
    dy = abs(B[1]-A[1])
    s1 = Sign(B[0]-A[0])
    s2 = Sign(B[1]-A[1])
    if dy > dx:
        dx ,dy = dy, dx
        Inter = 1
    else :
        Inter = 0
    e = 2*dy - dx
    i = 0
    for i in range(1, dx):
        pts.append([x,y])
        while e > 0:
            if Inter == 1 :
                x += s1
            else :
                y += s2
            e -= 2*dx
        if Inter == 1:
            y += s2
        else :
            x += s1
        e += 2*dy
    return pts

def edge(A):
    glBegin(GL_POINTS)
    for x, y in A:
        glVertex2f(x,y)
    glEnd()

def drawSeg(A):
    for i in A:
        edge(line(i[0],i[1]))

def drawCir(A):
    glPointSize(8)
    glBegin(GL_TRIANGLE_FAN)
    for i in range(0,360):
        glVertex2f(A[0]+30*cos(radians(i)),A[1]+30*sin(radians(i)))
    glEnd()

def drawClock():
    glClear(GL_COLOR_BUFFER_BIT)
    global HZ, HO, MZ, MO, SZ, SO, C1, C2, C3, C4, H0, H1, M0, M1, S0, S1
    glColor3f(0.0,0.0,0.0)
    glPointSize(8)
    drawSeg(HZ.getSeg(H0))
    drawSeg(HO.getSeg(H1))
    drawCir(C1)
    drawCir(C2)
    glPointSize(8)
    drawSeg(MZ.getSeg(M0))
    drawSeg(MO.getSeg(M1))
    drawCir(C3)
    drawCir(C4)
    glPointSize(8)
    drawSeg(SZ.getSeg(S0))
    drawSeg(SO.getSeg(S1))
    glutSwapBuffers()
    glFlush()

def update(val):
    time = datetime.now().strftime("%H:%M:%S").split(':')
    global H0, H1, M0, M1, S0, S1
    glutPostRedisplay()
    glutTimerFunc(1000,update,0)
    H0 = int(int(time[0])/10)
    H1 = int(time[0])%10

    M0 = int(int(time[1])/10)
    M1 = int(time[1])%10

    S0 = int(int(time[2])/10)
    S1 = int(time[2])%10


def main():
    glutInit(argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(700,700)
    glutInitWindowPosition(110,55)
    glutCreateWindow("Digital Clock")
    glutDisplayFunc(drawClock)
    glutTimerFunc(0,update,0)
    glutIdleFunc(drawClock)

    init()
    glutMainLoop()

if __name__ == "__main__":
    main()