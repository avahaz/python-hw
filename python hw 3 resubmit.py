#1 ch 3 programming exercise 13
print("#1 ch 3 programming exercise 13")
def series_sum():
    n=eval(input("How many numbers are to be summed?: "))
    sum = 0
    for i in range(n):
        x=int(input("Enter the numbers: "))
        sum += x
    print("The sum is ",sum)
series_sum()                        


print()
print()


#2 ch 3 programming exercise 14
print("#2 ch 3 programming exercise 14")
def series_avg():
    n=eval(input("How many numbers will be averaged?: "))
    sum = 0
    for i in range(n):
        x=float(input("Enter the numbers: "))
        sum += x
        avg = sum/n
    print("The average is ", avg)
series_avg()

print()
print()


#3 ch 4 discussion problem 2 abcdefg
print("#3 ch 4 discussion problem 2 abcdefg")
import graphics
#a
print("a)")
from graphics import *
win=GraphWin()
p=Point(130,130)
p.draw(win)
print("You get one black pixel dot at the point (130,130) in the lower right quadrant on the graphics window")
#You get one black pixel dot at the point (130,130) in the lower right quadrant on the graphics window
print()
#b
print("b)")
c= Circle(Point(30,40),25)
c.setFill("blue")
c.setOutline("red")
c.draw(win)
print("You get a circle centered at point (30,40) with a radius of 25. The circle is filled in blue with a red outline and lies in the upper left hand quadrant of the plane.")
#You get a circle centered at point (30,40) with a radius of 25. The circle is filled in blue with a red outline and lies in the upper left hand quadrant of the plane.
print()
#c
print("c)")
r=Rectangle(Point(20,20),Point(40,40)) 
r.setFill(color_rgb(0,255,150)) 
r.setWidth(3)
r.draw(win)
print("You get a square with a thick black outline and filled color of a green. It lies in the upper left hand corner, 20 pixels tall and wide.")
#You get a square with a thick black outline and filled color of a green. It lies in the upper left hand corner, 20 pixels tall and wide.
print()
#d
print("d)")
l=Line(Point(100,100),Point(100,200)) 
l.setOutline("red4") 
l.setArrow("first")
l.draw(win)
print("You get a red arrow point upwards, stemming from the bottom of the plane ending at the center.")
#You get a red arrow point upwards, stemming from the bottom of the plane ending at the center.
print()
#e
print("e)")
oval=Oval(Point(50,50), Point(60,100)) 
oval.draw(win)
print("You get a thin, black outlined, vertical oval on the left side of the plane.")
#You get a thin, black outlined, vertical oval on the left side of the plane.
print()
#f
print("f)")
shape=Polygon(Point(5,5),Point(10,10),Point(5,10),Point(10,5)) 
shape.setFill("orange")
shape.draw(win)
print("You get a tiny hourglass figure in the far upper left corner. It is filled in orange and outlined in black.")
#You get a tiny hourglass figure in the far upper left corner. It is filled in orange and outlined in black.
print()
#g
print("g)")
t=Text(Point(100,100),"Hello World!") 
t.setFace("courier") 
t.setSize(16) 
t.setStyle("italic")
t.draw(win)
print("You get the phrase 'Hello World!' written in black courier font across the center of the plane.")
#You get the phrase "Hello World!" written in black courier font across the center of the plane.

print()
print()


#4 ch 4 discussion problem 3
print("#4 ch 4 discussion problem 3")
def main(): 
    win = GraphWin() 
    shape = Circle(Point(50,50),20) 
    shape.setOutline("red") 
    shape.setFill("red") 
    shape.draw(win) 
    for i in range(10): 
        p=win.getMouse() 
        c=shape.getCenter() 
        dx=p.getX()-c.getX()
        dy = p.getY()-c.getY() 
        shape.move(dx,dy) 
    win.close() 
main()
#A red outlined and filled circle with a radius of 20 appears in the upper the hand corner. It moves to the spot of each click of your mouse. After the 10th click, the window closes.
print("A red outlined and filled circle woth a radius of 20 appears in the upper the hand corner. It moves to the spot of each click of your mouse. After the 10th click, the window closes.")

print()
print()


#5 ch 4 programming exercise 2
print("#5 ch 4 programming exercise 2")
def target(): 
    win = GraphWin() 
    WC=Circle(Point(100,100),100)
    WC.setFill("white")
    WC.setOutline("black")
    WC.draw(win)
    BKC=Circle(Point(100,100),80)
    BKC.setFill("black")
    BKC.setOutline("black")
    BKC.draw(win)
    BLC=Circle(Point(100,100),60)
    BLC.setFill("blue")
    BLC.setOutline("blue")
    BLC.draw(win)
    RC=Circle(Point(100,100),40)
    RC.setFill("red")
    RC.setOutline("red")
    RC.draw(win)
    YC=Circle(Point(100,100),20)
    YC.setFill("yellow")
    YC.setOutline("yellow")
    YC.draw(win)
target()

print()
print()


#6 ch 4 programming exercise 3
print("#6 ch 4 programming exercise 3")
def face():
    win=GraphWin()
    eye1=Point(75,25)
    eye2=Point(125,25)
    mouth=Line(Point(75,50),Point(125,50))
    eye1.draw(win)
    eye2.draw(win)
    mouth.draw(win)
face()

print()
print()


#7 ch 4 programming exercise 8
print("#7 ch 4 programming exercise 8")
def line():
    win=GraphWin()
    p1=win.getMouse()
    x1=p1.getX()
    y1=p1.getY()
    p2=win.getMouse()
    x2=p2.getX()
    y2=p2.getY()
    aLine=Line(Point(x1,y1),Point(x2,y2))
    aLine.draw(win)
    dx=x2-x1
    dy=y2-y1
    m=dy/dx
    from math import sqrt
    length=sqrt(dx**2+dy**2)
    print("The length is", length, "and the slope is ", m)
line()



