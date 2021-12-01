#drawing a line using DDA

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import math

def init():
    glClearColor(1.0,2.0,1.0,1.0)
    gluOrtho2D(-100.0,100.0,-100.0,100.0)

x1 = 0
x2 = 0
y1 = 0
y2 = 0

def plotpoints():
    global x1, y1, x2, y2
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0,0.0,0.0)
    glPointSize(5.0)

    dx = x2 - x1 
    dy = y2 - y1 
    if abs(dx) > abs(dy): 
        steps = abs(dx)
    else:
        steps = abs(dy)
    
    ix = dx/steps 
    iy = dy/steps 
    x = x1 
    y = y1 
    glBegin(GL_POINTS)
    glVertex2f(x,y)
    glEnd()
    for i in range(abs(steps)+1):
        x = x + ix
        y = y + iy
        glBegin(GL_POINTS)
        glVertex2f(x,y)
        glEnd()
    glFlush()

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
    glutInitWindowSize(500,500)
    glutInitWindowPosition(50,50)
    glutCreateWindow("DDA")

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