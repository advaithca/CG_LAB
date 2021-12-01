# Bresenham line drawing algorithm

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import math

def init():
    glClearColor(1.0,1.0,1.0,1.0)
    gluOrtho2D(-100.0,100.0,-100.0,100.0)

x1 = 0
x2 = 0
y1 = 0
y2 = 0

def plotpoints():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0,0.0,0.0)
    glPointSize(6.0)

    x = x1
    y = y1

    dx = abs(x2 - x)
    dy = abs(y2 - y)
    s1 = (x2 - x1)/abs(x2 - x1) if x2 != x1 else 0
    s2 = (y2 - y1)/abs(y2 - y1) if y2 != y1 else 0

    if dy > dx:
        temp = dx
        dx = dy
        dy = temp
        I = 1
    else:
        I = 0
    
    p = 2 * dy - dx

    for i in range(1, dx):
        glBegin(GL_POINTS)
        glVertex2f(x,y)
        glEnd()
        while p > 0:
            if I == 1:
                x += s1
            else:
                y += s2
            p -= 2 * dx
        if I == 1:
            y += s2
        else:
            x += s1
        p += 2 * dy

    glFlush()

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
    glutInitWindowSize(500,500)
    glutInitWindowPosition(50,50)
    glutCreateWindow("Bresenham's Line drawing")

    global x1, x2, y1, y2

    print("Enter coordinates of end-points")
    x1 = int(input("X-coordinate of 1st point : "))
    y1 = int(input("Y-coordinate of 1st point : "))
    x2 = int(input("X-coordinate of 2nd point : "))
    y2 = int(input("Y-coordinate of 2nd point : "))
    
    glutDisplayFunc(plotpoints)
    init()
    glutMainLoop()

if __name__ == "__main__":
    main()