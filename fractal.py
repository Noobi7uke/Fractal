from tkinter import *
from math import sin, cos, sqrt
import time

def stroke(canvas,P1,P2,color,height):
    canvas.create_line(P1[0],height-P1[1],P2[0],height-P2[1],fill=color)

class Triangle:
    def __init__(self,P1,P2):
        self.p1=P1
        self.p2=P2
        dx = P2[0]-P1[0]
        dy = P2[1]-P1[1]
        self.p3 = (P1[0] + (dx-sqrt(3)*dy)/2,P1[1] + (dy+sqrt(3)*dx)/2)

    def draw(self,canvas,color):
        stroke(canvas,self.p1,self.p2,color,800)
        stroke(canvas,self.p2,self.p3,color,800)
        stroke(canvas,self.p1,self.p3,color,800)
    @classmethod
    def getThird(cls, P1, P2):
        dx = P2[0]-P1[0]
        dy = P2[1]-P1[1]
        return (P1[0] + (dx-sqrt(3)*dy)/2,P1[1] + (dy+sqrt(3)*dx)/2)


class Edge:
    def __init__(self,P1,P2):
        self.p1 = P1
        self.p2 = P2
    
    def draw(self,canvas,color):
        stroke(canvas,self.p1,self.p2,color,800)
    
    def split(self):
        print(self)
        X1,Y1 = self.p1
        X4,Y4 = self.p2
        X2,Y2 = ((2*X1+X4)/3,(2*Y1+Y4)/3)
        X3,Y3 = ((X1+2*X4)/3,(Y1+2*Y4)/3)
        return (Edge((X1,Y1),(X2,Y2)),Edge((X2,Y2),(X3,Y3)),Edge((X3,Y3),(X4,Y4)))

    def tri(self):
        X,Y = Triangle.getThird(self.p2,self.p1)
        return (Edge(self.p1,(X,Y)), Edge(self.p2,(X,Y)))

    def __str__(self):
        return f"<Edge - {self.p1} {self.p2}>"

def Snowflake_Edge(edge, n, canvas):
    if n==0:
        return 
    else:
        print("SE = ",edge);
        e1,e2,e3 = edge.split()
        print(e1,e2,e3)
        Snowflake_Edge(e1, n-1, canvas)
        f2,g2 = e2.tri()
        print(f2,g2)
        f2.draw(canvas,'red')
        g2.draw(canvas,'red')

        Snowflake_Edge(f2,n-1,canvas)
        Snowflake_Edge(g2,n-1,canvas)
        Snowflake_Edge(e3,n-1,canvas)
    
def Snowflake(N,canvas):
    P1 = (200,200)
    P2 = (800,200)
    P3 = Triangle.getThird(P1,P2)
    e1 = Edge(P1,P2)
    e2 = Edge(P2,P3)
    e3 = Edge(P3,P1)

    e1.draw(canvas,'red')
    e2.draw(canvas,'red')
    e3.draw(canvas,'red')

    Snowflake_Edge(e1, N-1, canvas)
    Snowflake_Edge(e2, N-1, canvas)
    Snowflake_Edge(e3, N-1, canvas)

def main():
    root = Tk()
    # set width and height of canvas
    w = 1000
    h = 800
    # create the canvas for drawing
    c = Canvas(width=w, height=h, bg='yellow')
    c.pack()
    color_list = ['blue', 'red', 'black']
    for i in range(1,6):
        Snowflake(i,c)
        root.update()
        time.sleep(0.5)
    root.mainloop()


if __name__=="__main__":
    main()
