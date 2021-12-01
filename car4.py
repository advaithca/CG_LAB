# Animates a car

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from sys import argv
from math import atan, cos, sin, radians, tan
from win32api import Beep

# Car Stuff
XL = 10
YB = 40
XLM = XL + 100
YM = YB + 100
XLT = XLM + 15
YT = YM + 75
XRT = XLT + 170
XRM = XRT + 15
XR = XRM + 100
J = 0

XC1 = XL + 60
YC1 = YC2 = YB
XC2 = XR - 60
R = 40
S = float(input("Speed :: "))
# End Car Stuff

H = 1

# Line stuff
t = float(input("Angle of Inclination :: "))
m = tan(radians(t))
x1 = 1000 if m > 0 else -1000 if m < 0 else 1000
y1 = m*x1
x2 = -x1
y2 = -y1
# End Line stuff

def init():
    glClearColor(1.0,1.0,1.0,0.0)
    gluOrtho2D(-1000,1000,-1000,1000)

def drawLine():
    global x1, y1, x2, y2
    glLineWidth(5.0)
    glColor3f(0.0,0.0,0.0)
    glBegin(GL_LINES)
    glVertex2f(x1,y1)
    glVertex2f(x2,y2)
    glEnd()
p = 0
def drawCar():
    global XL, YB, XLM, YM, XLT, YT, XRT, XRM, XR, XC1, XC2, YC1, YC2, R, J, t
    D = radians(t)
    glClear(GL_COLOR_BUFFER_BIT)
    drawLine()
    glColor3f(sin(D+J),cos(D-J),tan(D+2*J))
    glBegin(GL_POLYGON)
    glVertex2f(XL*cos(D) - YB*sin(D), XL*sin(D) + YB*cos(D))
    glVertex2f(XL*cos(D) - YM*sin(D), XL*sin(D) + YM*cos(D))
    glVertex2f(XLM*cos(D) - YM*sin(D),XLM*sin(D) + YM*cos(D))
    glVertex2f(XLT*cos(D) - YT*sin(D),XLT*sin(D) + YT*cos(D))
    glVertex2f(XRT*cos(D) - YT*sin(D),XRT*sin(D) + YT*cos(D))
    glVertex2f(XRM*cos(D) - YM*sin(D),XRM*sin(D) + YM*cos(D))
    glVertex2f(XR*cos(D) - YM*sin(D),XR*sin(D) + YM*cos(D))
    glVertex2f(XR*cos(D) - YB*sin(D),XR*sin(D) + YB*cos(D))
    glEnd()

    glColor3f(0.0,0.0,1.0)
    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(XC1*cos(D) - YC1*sin(D),XC1*sin(D) + YC1*cos(D))
    for i in range(0,361):
        theta = radians(i)
        if (i+J)%361 <= 120:
            glColor3f(1.0,0.0,0.0)
        elif (i+J)%361 > 120 and (i+J)%361 <= 240:
            glColor3f(0.0,1.0,0.0)
        elif (i+J)%361 > 240 and (i+J)%361 <= 360:
            glColor3f(0.0,0.0,1.0)
        xc = XC1 + R * cos(theta)
        yc = YC1 + R * sin(theta)
        glVertex2f(xc*cos(D) - yc*sin(D),xc*sin(D) + yc*cos(D))
    glEnd()
    glColor3f(0.0,0.0,1.0)
    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(XC2*cos(D) - YC2*sin(D),XC2*sin(D) + YC2*cos(D))
    for i in range(0,361):
        theta = radians(i)
        if (i+J)%361 <= 120:
            glColor3f(1.0,0.0,0.0)
        elif (i+J)%361 > 120 and (i+J)%361 <= 240:
            glColor3f(0.0,1.0,0.0)
        elif (i+J)%361 > 240 and (i+J)%361 < 361:
            glColor3f(0.0,0.0,1.0)
        xc = XC2 + R * cos(theta)
        yc = YC2 + R * sin(theta)
        glVertex2f(xc*cos(D) - yc*sin(D),xc*sin(D) + yc*cos(D))
    glEnd()
    glFlush()

s = S

def Controller(*args):
    global XL, YB, XLM, YM, XLT, YT, XRT, XRM, XR, XC1, XC2, YC1, YC2, R, J, m, s, t
    if args[0] == b'w' or args[0] == b'W':
        s *= 1.1
    if args[0] == b'S' or args[0] == b's':
        s *= 0.9
    if args[0] == b'h':
        print('\a')
        Beep(5000,500)
        # playsound.playsound(r"D:\Music\VAR\Duality.mp3", block=False)
    if args[0] == b'a':
        t += 1
    if args[0] == b'd':
        t -= 1
    glutPostRedisplay()

def update(value):
    glutPostRedisplay()
    glutTimerFunc(int(1000/120),update,0)
    global XL, YB, XLM, YM, XLT, YT, XRT, XRM, XR, XC1, XC2, YC1, YC2, R, J, s, H, t, m, x1, x2, y1, y2
    m = tan(radians(t))
    x1 = 1000 if m > 0 else -1000 if m < 0 else 1000
    y1 = m*x1
    x2 = -x1
    y2 = -y1
    if XR < 1200 and H == 1 :
        s -= 0.001
        J += 5*s
        XL += 5*s
        XLM += 5*s
        XLT += 5*s
        XRT += 5*s
        XRM += 5*s
        XR += 5*s
        XC1 += 5*s
        XC2 += 5*s
    if XR >= 1200 and H == 1 :
        H = -1
    if  XL > -1200 and H == -1:
        s += 0.001
        J -= 5*s
        XL -= 5*s
        XLM -= 5*s
        XLT -= 5*s
        XRT -= 5*s
        XRM -= 5*s
        XR -= 5*s
        XC1 -= 5*s
        XC2 -= 5*s
    if XL <= -1200 and H == -1:
        H = 1

def main():
    glutInit(argv)
    glutInitDisplayMode(GLUT_RGB | GLUT_SINGLE)
    glutInitWindowPosition(75,80)
    glutInitWindowSize(800,800)
    glutCreateWindow("Car")
    glutDisplayFunc(drawCar)
    glutKeyboardFunc(Controller)
    glutTimerFunc(0,update,0)
    glutIdleFunc(drawCar)
    init()
    glutMainLoop()

if __name__ == "__main__":
    print("W to go forwards\nS to go backwards\nH to honk\nA to increase angle\nD to decrease angle")
    main()
