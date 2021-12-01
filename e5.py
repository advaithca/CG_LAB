#Program to do some 2D transformations

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import math

x1 = 0.0
x2 = 0.0
x3 = 0.0
y1 = 0.0
y2 = 0.0
y3 = 0.0
vx = 0
vy = 0
r = 0
theta = 0
xa = 0.0
xb = 0.0
ya = 0.0
yb = 0.0
m = 0.0
c = 0.0

def init():
    glClearColor(1.0,2.0,1.0,1.0)
    gluOrtho2D(-100.0,100.0,-100.0,100.0)

def plotAxes():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0.0,0.0,0.0)
    glBegin(GL_LINES)
    glVertex2f(-100,0)
    glVertex2f(100,0)
    glEnd()
    glBegin(GL_LINES)
    glVertex2f(0,-100)
    glVertex2f(0,100)
    glEnd()

def Translate():
    points = [[x1,y1],[x2,y2],[x3,y3]]
    newones = []

    for p in points:
        newones.append([p[0]+vx,p[1]+vy])
    print(newones)

    glPointSize(6.0)
    plotAxes()

    glColor3f(0.0,0.0,1.0)
    glPointSize(6.0)
    glBegin(GL_LINES)
    glVertex2f(x1,y1)
    glVertex2f(x2,y2)
    glEnd()
    glBegin(GL_LINES)
    glVertex2f(x2,y2)
    glVertex2f(x3,y3)
    glEnd()
    glBegin(GL_LINES)
    glVertex2f(x3,y3)
    glVertex2f(x1,y1)
    glEnd()
    
    glColor3f(1.0,0.0,0.0)
    glBegin(GL_LINES)
    glVertex2f(newones[0][0],newones[0][1])
    glVertex2f(newones[1][0],newones[1][1])
    glEnd()
    glBegin(GL_LINES)
    glVertex2f(newones[1][0],newones[1][1])
    glVertex2f(newones[2][0],newones[2][1])
    glEnd()
    glBegin(GL_LINES)
    glVertex2f(newones[2][0],newones[2][1])
    glVertex2f(newones[0][0],newones[0][1])
    glEnd()

    glFlush()

def Rotate():
    points = [[x1,y1],[x2,y2],[x3,y3]]
    newones = []

    if r == 1:
        for p in points:
            newones.append([p[0]*math.cos(theta) - p[1]*math.sin(theta),p[0]*math.sin(theta) + p[1]*math.cos(theta)])
    elif r == 2:
        for p in points:
            newones.append([(p[0]-xa)*math.cos(theta) - (p[1]-ya)*math.sin(theta) + xa,(p[0]-xa)*math.sin(theta) + (p[1]-ya)*math.cos(theta) + ya])
    glPointSize(3.0)
    
    plotAxes()

    glColor3f(0.0,0.0,1.0)
    glPointSize(6.0)
    glBegin(GL_LINES)
    glVertex2f(x1,y1)
    glVertex2f(x2,y2)
    glEnd()
    glBegin(GL_LINES)
    glVertex2f(x2,y2)
    glVertex2f(x3,y3)
    glEnd()
    glBegin(GL_LINES)
    glVertex2f(x3,y3)
    glVertex2f(x1,y1)
    glEnd()
    
    glColor3f(1.0,0.0,0.0)
    glBegin(GL_LINES)
    glVertex2f(newones[0][0],newones[0][1])
    glVertex2f(newones[1][0],newones[1][1])
    glEnd()
    glBegin(GL_LINES)
    glVertex2f(newones[1][0],newones[1][1])
    glVertex2f(newones[2][0],newones[2][1])
    glEnd()
    glBegin(GL_LINES)
    glVertex2f(newones[2][0],newones[2][1])
    glVertex2f(newones[0][0],newones[0][1])
    glEnd()
    glFlush()

def Scale():
    points = [[x1,y1],[x2,y2],[x3,y3]]
    newones = []

    if r == 1:
        for p in points:
            newones.append([p[0]*vx,p[1]*vy])
    elif r == 2:
        for p in points:
            newones.append([(p[0]-xa)*vx + xa,(p[1]-ya)*vy + ya])

    glPointSize(3.0)
    
    plotAxes()

    glColor3f(0.0,0.0,1.0)
    glPointSize(6.0)
    glBegin(GL_LINES)
    glVertex2f(x1,y1)
    glVertex2f(x2,y2)
    glEnd()
    glBegin(GL_LINES)
    glVertex2f(x2,y2)
    glVertex2f(x3,y3)
    glEnd()
    glBegin(GL_LINES)
    glVertex2f(x3,y3)
    glVertex2f(x1,y1)
    glEnd()
    
    glColor3f(1.0,0.0,0.0)
    glBegin(GL_LINES)
    glVertex2f(newones[0][0],newones[0][1])
    glVertex2f(newones[1][0],newones[1][1])
    glEnd()
    glBegin(GL_LINES)
    glVertex2f(newones[1][0],newones[1][1])
    glVertex2f(newones[2][0],newones[2][1])
    glEnd()
    glBegin(GL_LINES)
    glVertex2f(newones[2][0],newones[2][1])
    glVertex2f(newones[0][0],newones[0][1])
    glEnd()
    glFlush()

def Reflect():
    points = [[x1,y1],[x2,y2],[x3,y3]]
    newones = []
    
    for p in points:
        if r == 1:
            newones.append([p[0], -p[1]])
        elif r == 2:
            newones.append([-p[0], p[1]])
        elif r == 3:
            newones.append([-p[0], -p[1]])
        elif r == 4:
            newones.append([p[1], p[0]])        
        elif r==5:
            newones.append([-p[1], -p[0]])
        elif r == 6:
            newones.append([((1 - m**2)*p[0] + 2 * m * (p[1] - c))/(1 + m**2), ( 2 * m * p[0] - ( 1 - m**2)*p[1] + 2 * c)/(1 + m**2)])
            
    glPointSize(3.0)
    
    plotAxes()

    glColor3f(0.0,0.0,1.0)
    glPointSize(6.0)
    glBegin(GL_LINES)
    glVertex2f(x1,y1)
    glVertex2f(x2,y2)
    glEnd()
    glBegin(GL_LINES)
    glVertex2f(x2,y2)
    glVertex2f(x3,y3)
    glEnd()
    glBegin(GL_LINES)
    glVertex2f(x3,y3)
    glVertex2f(x1,y1)
    glEnd()
    
    glColor3f(1.0,0.0,0.0)
    glBegin(GL_LINES)
    glVertex2f(newones[0][0],newones[0][1])
    glVertex2f(newones[1][0],newones[1][1])
    glEnd()
    glBegin(GL_LINES)
    glVertex2f(newones[1][0],newones[1][1])
    glVertex2f(newones[2][0],newones[2][1])
    glEnd()
    glBegin(GL_LINES)
    glVertex2f(newones[2][0],newones[2][1])
    glVertex2f(newones[0][0],newones[0][1])
    glEnd()

    if r == 4:
        glColor3f(0.0,1.0,0.0)
        glBegin(GL_LINES)
        glVertex2f(100.0,100.0)
        glVertex2f(-100.0,-100.0)
        glEnd()
    elif r == 5:
        glColor3f(0.0,1.0,0.0)
        glBegin(GL_LINES)
        glVertex2f(-100.0,100.0)
        glVertex2f(100.0,-100.0)
        glEnd()
    elif r == 6:
        glColor3f(0.0,1.0,0.0)
        glBegin(GL_LINES)
        glVertex2f(xa,ya)
        glVertex2f(xb,yb)
        glEnd()
    glFlush()

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
    glutInitWindowSize(1000,800)
    glutInitWindowPosition(50,50)
    glutCreateWindow("2D Transformations")

    global x1,y1,x2,y2,x3,y3,vx,vy,r,theta,xa,xb,ya,yb,m,c

    print("\nEnter co-ordinate of one point of the equilateral triangle ::")
    x1 = float(input("\nx co-ordinate :: "))
    y1 = float(input("\ny co-ordinate :: "))

    a = float(input("\nEnter value of side :: "))

    x2 = x1 + a
    y2 = y1

    x3 = x1 + a/2
    y3 = y1 + math.sqrt(3)*a/2

    print("\n Choose transformation :: ")
    print("\n1 . Translation")
    print("\n2 . Rotation")
    print("\n3 . Scaling")
    print("\n4 . Reflection")

    ch = int(input("\nYour Choice :: "))

    if ch == 1:
        vx = float(input("\nTranslation along x-axis value :: "))
        vy = float(input("\nTranslation along y-axis value :: "))
        glutDisplayFunc(Translate)
    elif ch == 2:
        theta = float(input("\nEnter Rotation angle in degrees :: "))
        theta = (math.pi/180)*theta
        print("\nRotate about :: ")
        print("\n1. Origin")
        print("\n2. A reference point")
        r = int(input("\nYour Choice ::"))
        if r == 2:
            xa = float(input("\nx co-ordinate of reference point :: "))
            ya = float(input("\ny co-ordinate of reference point :: "))
        glutDisplayFunc(Rotate)
    elif ch == 3:
        print("\nScale with respect to :: ")
        print("\n1. Origin")
        print("\n2. A reference point")
        r = int(input("\nYour Choice ::"))
        vx = float(input("\nScaling factor for x-cordinate :: "))
        vy = float(input("\nScaling factor for y-cordinate :: "))
        if r == 2:
            xa = float(input("\nx co-ordinate of reference point :: "))
            ya = float(input("\ny co-ordinate of reference point :: "))
        glutDisplayFunc(Scale)
    elif ch == 4:
        print("\nReflect about : ")
        print("\n1. X-axis")
        print("\n2. Y-axis")
        print("\n3. Origin")
        print("\n4. the line x = y")
        print("\n5. the line x = -y")
        print("\n6. Reflect about an arbitrary line")
        r = int(input("\nYour Choice ::"))
        if r == 6:
            xa = float(input("\nx co-ordinate of first point :: "))
            ya = float(input("\ny co-ordinate of first point :: "))
            xb = float(input("\nx co-ordinate of second point :: "))
            yb = float(input("\ny co-ordinate of second point :: "))
            m = (yb - ya)/(xb - xa)
            c = ya - xa*m
        glutDisplayFunc(Reflect)

    init()
    glutMainLoop()

if __name__ == "__main__":
    main()