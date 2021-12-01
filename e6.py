from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import * 
import math

GX = 0
GY = 0
FPS=60
HALF = 1

print("\n\tPendulum Settings:\n\t=================")

LENGTH = float(input("\n\tPendulum Length (<500): "))
BOB_RADIUS =  float(input("\n\tBob Radius (<250): "))
MAX_THETA =  float(input("\n\tMax Displacement Angle (In degrees): "))
THETA = MAX_THETA
TIME_PERIOD =  2*math.pi*(math.sqrt(LENGTH/9.8))
SPEED_MULTIPLIER =  float(input("\n\tSpeed Multiplier: "))
THETA_INCREMENT =  (math.cos(math.radians(THETA))*SPEED_MULTIPLIER)-(math.cos(math.radians(MAX_THETA))*(SPEED_MULTIPLIER*0.9))


def init():
    glClearColor(1.0,2.0,1.0,0.0) 
    gluOrtho2D(-500,500,-500,500) 

def update(value):
    global GX, GY, LENGTH, HALF, THETA, MAX_THETA, THETA_INCREMENT
    glutPostRedisplay()
    glutTimerFunc(int(1000/FPS),update,int(0))
    if(HALF == 1):
        if(THETA<MAX_THETA):
            THETA = THETA + (THETA_INCREMENT)
        else:
            HALF=-1
    elif(HALF == -1):
        if(THETA>=-MAX_THETA):
            THETA = THETA - (THETA_INCREMENT)

        else:
            HALF=1
    GX = LENGTH * math.sin(math.radians(THETA))
    GY = - (LENGTH * math.cos(math.radians(THETA)))
    THETA_INCREMENT =  (math.cos(math.radians(THETA))*SPEED_MULTIPLIER)-(math.cos(math.radians(MAX_THETA))*(SPEED_MULTIPLIER*0.9))

def Circle(x,y):
    glPointSize(2.0)
    glBegin(GL_POINTS)
    theta = 0
    for i in range(0,360):
        theta = i * 180 / math.pi
        xc = x + BOB_RADIUS * math.cos(theta)
        yc = y + BOB_RADIUS * math.sin(theta)
        glVertex2f(xc,yc)
    glEnd()
    glFlush()

def Pendulum():
    glClear(GL_COLOR_BUFFER_BIT) 
    glColor3f(0.0,0.0,1.0) 
    glLineWidth(2)
    glBegin(GL_LINES)
    glVertex2f(0,0)
    glVertex2f(GX,GY)
    glEnd()
    Circle(GX,GY)
    glutSwapBuffers()

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGB  | GLUT_DOUBLE)
    glutInitWindowSize(500,500)
    glutInitWindowPosition(50,50)
    glutCreateWindow("Pendulum Animation")
    glutDisplayFunc(Pendulum)
    glutTimerFunc(0,update,0)
    glutIdleFunc(Pendulum)

    init()
    glutMainLoop()

if __name__ == "__main__":
    main()
