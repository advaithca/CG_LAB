# Program to animate a fan

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from sys import argv
from math import radians, cos, sin, sqrt

def rotate(T,theta):
    U = []
    for [i,j] in T:
        U.append([i*cos(theta)-j*sin(theta),i*sin(theta)+j*cos(theta)])
    return U

# Fan wings
S = 500
H = S*sqrt(3)/2
P = S/5
A = [[0,0],[-P,H],[P,H]]
B = rotate(A,radians(120))
C = rotate(A,radians(240))
THETA = 0
J = 0

def init():
    glClearColor(1.0,1.0,1.0,1.0)
    gluOrtho2D(-1000,1000,-1000,1000)

def drawFan():
    global A, B, C, J
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0,0.0,0.0)
    glBegin(GL_POLYGON)
    for [i,j] in A:
        glVertex2f(i,j)
    glEnd()
    glColor3f(0.0,1.0,0.0)
    glBegin(GL_POLYGON)
    for [i,j] in B:
        glVertex2f(i,j)
    glEnd()
    glColor3f(0.0,0.0,1.0)
    glBegin(GL_POLYGON)
    for [i,j] in C:
        glVertex2f(i,j)
    glEnd()
    glColor3f(0.0,0.0,0.0)
    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(0,0)
    for i in range(0,361):
        theta = radians(i)
        xc =  75 * cos(theta)
        yc =  75 * sin(theta)
        glVertex2f(xc,yc)        
    glEnd()
    glutSwapBuffers()
    glFlush()

def update(value):
    global A, B, C, THETA, J
    J += 1
    h = 1
    glutPostRedisplay()
    glutTimerFunc(int(30),update,0)
    THETA = THETA + 1 if h == 1 else THETA - 1
    if THETA > 180:
        h = -1
    elif THETA <= 180:
        h = 1
    t = radians(THETA)
    A = rotate(A, t)
    B = rotate(B, t)
    C = rotate(C, t)

def main():
    glutInit(argv)
    glutInitDisplayMode(GLUT_RGB | GLUT_DOUBLE)
    glutInitWindowPosition(80,55)
    glutInitWindowSize(750,750)
    glutCreateWindow("FAN")
    glutDisplayFunc(drawFan)
    glutTimerFunc(0,update,0)
    glutIdleFunc(drawFan)

    init()
    glutMainLoop()

if __name__ == "__main__":
    main()
