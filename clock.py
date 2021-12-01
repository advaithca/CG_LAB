# Program to animate a clock
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from sys import argv
from math import radians, cos, sin, tan

# Settings for the clock
R = 700
XH, XM, XS, YH, YM, YS = 0, 0, 0, R-200, R-100, R-50
THETA = 90
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
    global R, XH, XM, XS, YH, YM, YS, THETA, counts, countm, counth, JS, JM, JH
    glutPostRedisplay()
    glutTimerFunc(1,update,0)    
    XS = (R-50)*cos(radians(THETA-JS))
    YS = (R-50)*sin(radians(THETA-JS))
    JS += 6
    counts = counts + 1
    if counts == 60:
        counts = 0
        countm += 1
        XM = (R-100)*cos(radians(THETA-JM))
        YM = (R-100)*sin(radians(THETA-JM))
        JM += 6

    if countm == 60:
        countm = 0
        counth += 1
        XH = (R-200)*cos(radians(THETA-JH))
        YH = (R-200)*sin(radians(THETA-JH))
        JH += 30
    
    if counth == 12:
        counts = 0
        countm = 0
        counth = 0

    if JS == 360:
        JS = 0
    if JM == 360:
        JM = 0
    if JH == 360:
        JH = 0

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
