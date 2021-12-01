# menu driven program to draw  a circle using 
# A) Mid point circle drawing algorithm 
# B) Polar circle generation algorithm
# C) Non-Polar circle generation algorithm

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
from math import pi, sin, cos, sqrt

xc = 0
yc = 0
r = 0

def init():
    glClearColor(1.0,2.0,1.0,1.0)
    gluOrtho2D(-100.0,100.0,-100.0,100.0)

def midpoint():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0,0.0,0.0)
    glPointSize(5.0)
    glBegin(GL_POINTS)

    x = 0
    y = r
    glVertex2f(x+xc, y+yc)
    p = 5/4 - r
    
    while x < y:
        x += 1
        if p < 0:
            p += 2*x + 1
        else:
            y -= 1
            p += 2 * (x - y) + 1
        glVertex2f(x+xc,y+yc)
        glVertex2f(-x+xc,-y+yc)
        glVertex2f(x+xc,-y+yc)
        glVertex2f(-x+xc,y+yc)
        glVertex2f(y+xc,x+yc)
        glVertex2f(-y+xc,-x+yc)
        glVertex2f(-y+xc,x+yc)
        glVertex2f(y+xc,-x+yc)
    glEnd()
    glFlush()

def pol():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0,0.0,0.0)
    glPointSize(5.0)
    glBegin(GL_POINTS)
    theta = 0
    for i in range(0,360):
        theta = i * 180 / pi
        x = xc + r * cos(theta)
        y = yc + r * sin(theta)
        glVertex2f(x,y)
    glEnd()
    glFlush()

def npol():
    global xc, yc, r
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0,0.0,0.0)
    glPointSize(5.0)
    glBegin(GL_POINTS)

    for i in range(0,1000):
        y = i
        d = abs(r**2-(y)**2)
        x = sqrt(d)
        glVertex2f(x+xc,y+yc)
    glEnd()
    glFlush()

def main():    
    global xc, yc, r
    t = True
    while t:
        print("\n\nDraw a Circle using : ")
        print("1. Mid-Point circle drawing algorithm")
        print("2. Polar circle generation algorithm")
        print("3. Non-Polar circle generation algorithm")
        print("4. Exit")

        ch = int(input("\n Your Choice :: "))
        
        global r, xc, yc
        r = float(input("Enter radius : "))
        xc = float(input("Enter X co-ordinate of the centre : "))
        yc = float(input("Enter Y co-ordinate of the centre : "))

        glutInit(sys.argv)
        glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
        glutInitWindowSize(500,500)
        glutInitWindowPosition(50,50)
        glutCreateWindow("Drawing a Circle")

        if ch == 1:
            glutDisplayFunc(midpoint)
        elif ch == 2:
            glutDisplayFunc(pol)
        elif ch == 3:
            glutDisplayFunc(npol)
        else:
            t = False
        init()
        glutMainLoop()
    print("Ending...")

if __name__ == "__main__":
    main()