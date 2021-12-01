from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from math import pi, radians, cos, sin, atan, tan
import sys

NL = "\n\t"
print(f"\n{NL}ROLLING BALL{NL}============")
# PLANE STUFF
THETA = float(input(f"{NL}Enter Angle of inclination of the plane :: "))
x1 = -1000
y1 = tan(radians(THETA))*x1
x2 = -x1
y2 = -y1

# BALL STUFF
R = float(input(f"{NL}Radius of the ball :: "))
SM = float(input(f"{NL}Speed Multiplier for the ball :: "))
### Co-ordinates of ball
X = R 
Y = R
J = 0
### Denotes forward half (1) or backward half (-1)
H = 1 

def drawLine():
    global x1, y1, x2, y2
    glColor3f(0.0,0.0,0.0)
    glLineWidth(10.0)
    glBegin(GL_LINES)
    glVertex2f(x1,y1)
    glVertex2f(x2,y2)
    glEnd()


def drawBall(x, y):
    global J, R
    glLineWidth(10.0)
    glBegin(GL_TRIANGLE_FAN)
    theta = 0
    glVertex2f(x,y)
    for i in range(0,361):
        theta = radians(i)
        if (i+J)%361 < 120:
            glColor3f(1.0,0.0,0.0)
        elif (i+J)%361 == 120:
            glColor3f(0.0,0.0,0.0)
        elif (i+J)%361 > 120 and (i+J)%361 < 240:
            glColor3f(0.0,1.0,0.0)
        elif (i+J)%361 == 240:
            glColor3f(0.0,0.0,0.0)
        elif (i+J)%361 > 240 and (i+J)%361 < 361:
            glColor3f(0.0,0.0,1.0)
        elif (i+J)%361 == 0:
            glColor3f(0.0,0.0,0.0)
        xc = x + R * cos(theta)
        yc = y + R * sin(theta)
        glVertex2f(xc,yc)        
    glEnd()
    glPointSize(1.0)
    glColor3f(0.0,0.0,0.0)
    glBegin(GL_POINTS)
    theta = 0
    i = 0
    xc = 0
    yc = 0
    for i in range(0,360):
        theta = radians(i)
        xc = x + R * cos(theta)
        yc = y + R * sin(theta)
        glVertex2f(xc,yc)        
    glEnd()

def init():
    glClearColor(1.0,1.0,1.0,1.0)
    gluOrtho2D(-1000,1000,-1000,1000)

def plot():
    global R, THETA, X, Y
    t = radians(THETA)
    glClear(GL_COLOR_BUFFER_BIT)
    drawLine()
    drawBall(X*cos(t)-Y*sin(t), X*sin(t)+Y*cos(t))
    glFlush()
    glutSwapBuffers()

def update(value):
    global R, X, Y, THETA, SM, H, J
    glutPostRedisplay()
    glutTimerFunc(int(1000/59), update, int(0))
    A = 0.8 if tan(radians(THETA)) < 0 else 1.2
    B = 1.2 if tan(radians(THETA)) < 0 else 0.8
    A *= cos(radians(THETA))
    B *= cos(radians(THETA))

    if H == 1:
        X += 1*SM*B
        # Y += 1*SM
        J += 1*SM*B 
    if H == -1:
        X -= 1*SM*A
        # Y -= 1*SM
        J -= 1*SM*A

    if H == 1 and X >= 1000:
        H = -1
    if H == -1 and X <= -1000:
        H = 1

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGB | GLUT_DOUBLE)
    glutInitWindowPosition(100,50)
    glutInitWindowSize(700,700)
    glutCreateWindow("Ball Roll")
    glutDisplayFunc(plot)
    glutTimerFunc(0,update,0)
    glutIdleFunc(plot)
    init()
    glutMainLoop()

if __name__ == "__main__":
    main()