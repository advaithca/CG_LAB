# menu driven program to draw an ellipse using 
#  a)polar ellipse drawing algorithm
#  b)non polar ellipse drawing algorithm

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
from math import pi, sin, cos, sqrt

xc = 0
yc = 0
rx = 0
ry = 0

def init():
    glClearColor(1.0,2.0,1.0,1.0)
    gluOrtho2D(-100.0,100.0,-100.0,100.0)

def pol():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0,0.0,0.0)
    glPointSize(5.0)
    glBegin(GL_POINTS)
    theta = 0
    for i in range(0,360):
        theta = i * 180 / pi
        x = xc + rx * cos(theta)
        y = yc + ry * sin(theta)
        glVertex2f(x,y)
    glEnd()
    glFlush()

def npol():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0,0.0,0.0)
    glPointSize(4.5)
    glBegin(GL_POINTS)
    
    x = 0
    y = ry
    glVertex2f(x+xc, y+yc)

    
    while 2 * ry**2 * x < 2 * rx**2 * y:
        x += 1 
        y = (ry/rx)*sqrt(abs(rx**2 - x**2))
        glVertex2f(x+xc, y+yc)        
        glVertex2f(x+xc, -y+yc)
        glVertex2f(-x+xc, y+yc)
        glVertex2f(-x+xc, -y+yc)
    
    while y > 0:
        y -= 1
        x = (rx/ry)*sqrt(abs(ry**2 - y**2))
        glVertex2f(x+xc, y+yc)        
        glVertex2f(x+xc, -y+yc)
        glVertex2f(-x+xc, y+yc)
        glVertex2f(-x+xc, -y+yc)
    
    glEnd()
    glFlush()

def main():    
    global xc, yc, rx, ry

    print("\n\nDraw an Ellipse using : ")
    print("1. Polar ellipse generation algorithm")
    print("2. Non-Polar ellipse generation algorithm")

    ch = int(input("\n Your Choice :: "))
    
    xc = float(input("Enter X co-ordinate of the centre : "))
    yc = float(input("Enter Y co-ordinate of the centre : "))
    rx = float(input("Enter semi-major axis : "))
    ry = float(input("Enter semi-minor axis : "))

    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
    glutInitWindowSize(500,500)
    glutInitWindowPosition(50,50)
    glutCreateWindow("Drawing an Ellipse")


    if ch == 1:
        glutDisplayFunc(pol)
    elif ch == 2:
        glutDisplayFunc(npol)
    
    init()
    glutMainLoop()
    print("Ending...")

if __name__ == "__main__":
    main()