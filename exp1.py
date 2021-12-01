from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys

def init():
    glClearColor(1.0,2.0,1.0,1.0)
    gluOrtho2D(-100.0,100.0,-100.0,100.0)

x = 0.0
y = 0.0
ux = 0
lx = 0
sy = 0

def horizontal():    
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0,0.0,0.0)
    glPointSize(4.5)
    glBegin(GL_POINTS)
            
    if ux < lx:
        print("Error: Upper Limit smaller than lower limit.")
        glEnd()
        glFlush()

    else :
        if  int(lx)>=-100 and int(ux)<=100 and int(sy)>=-100 and int(sy)<=100:
            for i in range(lx,ux):
                x = i
                y = sy
                glVertex2f(x,y)
            glEnd()
            glFlush()
        else :
            print("Not integer, Hence, Bye!!")
            glFlush()

sx = 0
uy = 0
ly = 0

def vertical():
    x = 0.0
    y = 0.0
    
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0,0.0,0.0)
    glPointSize(4.5)
    glBegin(GL_POINTS)
    
    
    if uy < ly:
        print("Error: Upper limit lesser than lower limit.")
        glEnd()
        glFlush()
    else:
        if  int(ly)>=-100 and int(uy)<=100 and int(sx)>=-100 and int(sx)<=100:
            for i in range(ly,uy):
                x = sx
                y = i
                glVertex2f(x,y)
            glEnd()
            glFlush()
        else :
            print("Not integer, Hence, Bye!!")
            glFlush()
    
x1 = 0
x2 = 0

def diagonal():
    x = 0
    y = 0
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0,0.0,0.0)
    glPointSize(4.5)
    glBegin(GL_POINTS)

    if x1 < x2:
        for i in range(x1,x2):
            x = i
            y = i
            glVertex2i(x, y)
    elif x1 > x2:
        for i in range(x2,x1):
            x = i
            y = i
            glVertex2i(x, y)
    glEnd()
    glFlush()

def main():
    print("\n\nChoose : ")
    print("1. Horizontal Line")
    print("2. Vertical Line") 
    print("3. Diagonal Line")

    c = int(input("Your choice :: "))
        
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
    glutInitWindowSize(360,360)
    glutInitWindowPosition(50,50)
    glutCreateWindow("Experiment 1's extention")
        
    if c == 1:
        global ux, lx, sy
        print("Please enter a number between -100 and 100 for the co-ordinates")
        ux = int(input("Upper limit X-axis : "))
        lx = int(input("Lower limit X-axis : "))
        sy = int(input("Y-coordinate : "))
        glutDisplayFunc(horizontal)
    elif c == 2:
        global sx, uy, ly
        print("Please enter a number between -100 and 100 for the co-ordinates")
        sx = int(input("X-coordinate : "))
        uy = int(input("Upper limit Y-axis : "))
        ly = int(input("Lower limit Y-axis : "))
        glutDisplayFunc(vertical)
    elif c == 3:
        global x1, x2
        print("Please enter a number between -10 and 10 for the co-ordinates of the diagonal line (for example, (5,10).)")
        x1 = int(input("Enter co-ordinate for one end of the line (for example, 5) : "))
        x2 = int(input("Enter co-ordinate for other end of the line (for example, 10) : "))
        glutDisplayFunc(diagonal)
        
    init()    
    glutMainLoop()
    print("\n\n Ending.")

if __name__ == "__main__":
    main()