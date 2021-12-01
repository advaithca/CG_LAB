# Mid point line drawing algorithm

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys

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
    glBegin(GL_POINTS)
    
    dx = (x2 - x1)
    dy = (y2 - y1)

    if dy > dx:
        x = y1
        y = x1
    else:
        x = x1
        y = y1

    glVertex2f(x,y)

    di = dy - dx
    # dd = 2 * (dy - dx)

    while x < x2:
        x += 1
        if di < 0:
            di = di + dy
        else:
            y += 1
            di = di + dy - dx
        if dy > dx:
            glVertex2f(x,y)
        else:
            glVertex2f(y,x)
    
    glEnd()
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