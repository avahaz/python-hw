#hw 2
print("hw 2")

#1 ch2 discussion problem 4 abcd
print("#1 ch2 discussion problem 4 abcd")

#a
for i in range(5):
    print(i*i)
#b
for d in [3,1,4,1,5]:
    print(d, end=" ")
#c
for i in range(4):
    print("Hello")
#d
for i in range(5):
    print(i,2**i)

print()
print()

#2 ch3 discussion 1 ace
print("#2 ch3 discussion 1 ace")
#a
print(4.0/10.0+3.5*2)
#c
print(abs(4-20//3)**3)
#e
print(3*10//3+10%3)

print()
print()


#3 ch3 discussion 2 bc
print("#3 ch3 discussion 2 bc")
#b
import math
print("(n*(n-1))/2")
#c
print("4*math.pi*r**2")

print()
print()


#4 ch3 discussion 4 bc
print("#4 ch3 discussion 4 bc")
#b
for i in [1,3,5,7,9]:
    print(i,":",i**3)
print(i)
#c
x=2
y=10
for j in range(0,y,x):
    print(j,end="")
    print(x+y)
print("done")

print()
print()


#5 ch3 programming exercise 6
print("#5 ch3 progamming exercise 6")
def slope():
    x1=eval(input("enter the first x coordinate: "))
    y1=eval(input("enter the first y coordinate: "))
    x2=eval(input("enter the second x coordinate: "))
    y2=eval(input("enter the second y coordinate: "))
    m=(y2-y1)/(x2-x1)
    print("the slope is: ",m)
slope()

print()
print()

#6 ch3 programming exercise 7
print("#6 ch3 programming exercise 7")
def distance():
    x1=eval(input("enter the first x coordinate: "))
    y1=eval(input("enter the first y coordinate: "))
    x2=eval(input("enter the second x coordinate: "))
    y2=eval(input("enter the second y coordinate: "))
    from math import sqrt
    d=sqrt((x2-x1)**2+(y2-y1)**2)
    print("the distance between the points is: ",d)
distance()













