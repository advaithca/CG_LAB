# Mid-point ellipse drawing algorithm

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys


xc = 0
yc = 0
rx = 0
ry = 0

def init():
    glClearColor(1.0,2.0,1.0,1.0)
    gluOrtho2D(-100.0,100.0,-100.0,100.0)


def plotpoints():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0,0.0,0.0)
    glPointSize(4.0)
    glBegin(GL_POINTS)

    x = 0
    y = ry
    glVertex2f(x+xc, y+yc)

    p1 = ry**2 - (rx**2)*ry + (1/4)*rx**2

    # px = 2 * ry**2 * x
    # py = 2 * rx**2 * y

    while 2 * ry**2 * x < 2 * rx**2 * y:
        if p1 < 0:
            x += 1
            #px += ry**2
            p1 += 2 * ry**2 * x + ry**2
        else:
            x += 1
            y -= 1
            # px += 2 * ry**2
            # py -= 2 * rx**2
            p1 += 2 * ry**2 * x - 2 * rx**2 * y + ry**2
        glVertex2f(x+xc,y+yc)
        glVertex2f(-x+xc,-y+yc)
        glVertex2f(-x+xc,y+yc)
        glVertex2f(x+xc,-y+yc)
    
    p2 = ry**2 * (x+1/2)**2 + rx**2 * (y-1)**2 - rx**2 * ry**2

    while y >= 0:
        if p2 > 0:
            y -= 1
            # py -= 2 * rx**2
            p2 += rx**2 - 2 * rx**2 * y
        else:
            x += 1
            y -= 1
            # 2 * ry**2 * x += 2 * ry**2
            # py -= 2 * rx**2
            p2 += 2 * ry**2 * x - 2 * rx**2 * y + rx**2
        glVertex2f(x+xc,y+yc)
        glVertex2f(-x+xc,-y+yc)
        glVertex2f(-x+xc,y+yc)
        glVertex2f(x+xc,-y+yc)
    glEnd()
    glFlush()

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
    glutInitWindowSize(500,500)
    glutInitWindowPosition(50,50)
    glutCreateWindow("Mid-pt Ellipse drawing")

    global xc, yc, rx, ry

    xc = float(input("Enter X co-ordinate of the centre : "))
    yc = float(input("Enter Y co-ordinate of the centre : "))
    rx = float(input("Enter value of rx : "))
    ry = float(input("Enter value of ry : "))

    glutDisplayFunc(plotpoints)
    init()
    glutMainLoop()

if __name__ == "__main__":
    main()