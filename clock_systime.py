# Program to animate a clock using system time
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from sys import argv
from math import radians, cos, sin, tan
from datetime import datetime

TIME = datetime.now().strftime("%H:%M:%S").split(':')

# Settings for the clock
R = 700
XH, XM, XS, YH, YM, YS = 0, 0, 0, R-200, R-100, R-50
HTHETA = 0
MTHETA = 0
STHETA = 0
JS = 6
JM = 6
JH = 30
counts = 1
countm = 1
counth = 1

def init():
    glClearColor(1.0,1.0,1.0,0.0)
    gluOrtho2D(-1000,1000,-1000,1000)

def update(value):
    global R, XH, XM, XS, YH, YM, YS, HTHETA, MTHETA, STHETA, TIME
    glutPostRedisplay()
    glutTimerFunc(1,update,0)    
    TIME = datetime.now().strftime("%H:%M:%S").split(':')
    HTHETA = radians((int(TIME[0])/12)*360-90)
    MTHETA = radians((int(TIME[1])/60)*360-90)
    STHETA = radians((int(TIME[2])/60)*360-90)

    XH = (R-200)*cos(-HTHETA)
    YH = (R-200)*sin(-HTHETA)
    XS = (R-50)*cos(-STHETA)
    YS = (R-50)*sin(-STHETA)
    XM = (R-100)*cos(-MTHETA)
    YM = (R-100)*sin(-MTHETA)

def drawCircles(x,y):
    glColor3f(1.0,0.0,0.0)
    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(x,y)
    for j in range(0,361):
        xc = x + 50*cos(radians(j))
        yc = y + 50*sin(radians(j))
        glVertex2f(xc, yc)
    glEnd()
    glFlush()

def drawClock():
    global R, XH, YH, XM, YM, XS, YS
    x, y = 0, 0
    glClear(GL_COLOR_BUFFER_BIT)    
    
    # Drawing clock face
    glColor3f(0.0,0.0,0.6)
    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(0,0)
    for i in range(0,361):
        theta = radians(i)
        x = (R+50)*cos(theta)
        y = (R+50)*sin(theta)
        glVertex2f(x, y)
    glEnd()

    glColor3f(1.0,1.0,0.0)
    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(0,0)
    for i in range(0,361):
        theta = radians(i)
        x = (R-50)*cos(theta)
        y = (R-50)*sin(theta)
        glVertex2f(x, y)
    glEnd()
    
    for j in range(0,361):
        if j%30 == 0:
            drawCircles(R*cos(radians(j)),R*sin(radians(j)))
    
    # Drawing the clock's hours hand
    glColor3f(0.0,0.0,0.0)
    glLineWidth(8.0)
    glBegin(GL_LINES)
    glVertex2f(0,0)
    glVertex2f(XH, YH)
    glEnd()

    # Drawing the clock's minutes hand
    glColor3f(1.0,0.0,0.0)
    glLineWidth(5.0)
    glBegin(GL_LINES)
    glVertex2f(0,0)
    glVertex2f(XM, YM)
    glEnd()
    
    # Drawing the clock's seconds hand
    glColor3f(0.0,1.0,0.0)
    glLineWidth(3.0)
    glBegin(GL_LINES)
    glVertex2f(0,0)
    glVertex2f(XS, YS)
    glEnd()

    glColor3f(0.0,0.0,1.0)
    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(0,0)
    for i in range(0,361):
        theta = radians(i)
        glVertex2f(40*cos(theta),40*sin(theta))
    glEnd()
    
    glFlush()
    glutSwapBuffers()


def main():
    glutInit(argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(700,700)
    glutInitWindowPosition(110,55)
    glutCreateWindow("Clock")
    glutDisplayFunc(drawClock)
    glutTimerFunc(0,update,0)
    glutIdleFunc(drawClock)

    init()
    glutMainLoop()

if __name__ == "__main__":
    print("Tick Tock, Tick Tock, Tick To..")
    main()