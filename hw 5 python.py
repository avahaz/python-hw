print("programming exercise 1")
print()
def OM():
    print("Old MacDonald had a farm, Ee-igh, Ee-igh, Oh!")
def cow():
    OM()
    print("And on that farm he had a cow, Ee-igh, Ee-igh, Oh!")
    print("With a moo, moo here and a moo, moo there.")
    print("Here a moo, there a moo, everywhere a moo, moo")
    OM()
def sheep():
    OM()
    print("And on that farm he had a sheep, Ee-igh, Ee-igh, Oh!")
    print("With a baa, baa here and a baa, baa there.")
    print("Here a baa, there a baa, everywhere a baa, baa")
    OM()
def duck():
    OM()
    print("And on that farm he had a duck, Ee-igh, Ee-igh, Oh!")
    print("With a quack, quack here and a quack, quack there.")
    print("Here a quack, there a quack, everywhere a quack, quack")
    OM()
def chicken():
    OM()
    print("And on that farm he had a chicken, Ee-igh, Ee-igh, Oh!")
    print("With a cluck, cluck here and a cluck, cluck there.")
    print("Here a cluck, there a cluck, everywhere a cluck, cluck")
    OM()
def dog():
    OM()
    print("And on that farm he had a dog, Ee-igh, Ee-igh, Oh!")
    print("With a woof, woof here and a woof, woof there.")
    print("Here a woof, there a woof, everywhere a woof, woof")
    OM()
def main():
    cow()
    print()
    sheep()
    print()
    duck()
    print()
    chicken()
    print()
    dog()
main()

print()
print()
print()
print()
print("programming exercise 14 from ch.3")
def main():
    print("This program will find the average of your number set.")
    print("How many numbers are in your set?")
    sum=0.0
    count=0
    while True:
        n=float(input("Enter a number:"))
        sum=sum+n
        count=count+1
        choice = input("Add a number? (y/n):")
        if choice.casefold()=='n':
            break
    average=float(sum/count)
    print("average:", average)
main()


print()
print()
print()
print()
print("programming exercise 8 from ch 4")
import graphics
win=graphics.GraphWin()
from graphics import*
p1=win.getMouse()
p1.draw(win)
p2=win.getMouse()
p2.draw(win)
x1=p1.getX()
y1=p1.getY()
x2=p2.getX()
y2=p2.getY()
aline=Line((p1),(p2))
aline.draw(win)
p3=aline.getCenter()
p3.setOutline("cyan")
def main():
    dx=x2-x1
    dy=y2-y1
    slope=dy/dx
    length=math.sqrt((dx**2)+(dy**2))
    print("Length:", length)
    print("Slope:",slope)
main()


print()
print()
print()
print()
print("programming exercise #12, ch 6")
sumList(nums)
def sum(nums):
    input(num1,num2)
    sum=(num1+num2)
    print("The sum is", sum)
sum(nums)

print()
print()
print()
print()
print("#5, get some strings")
def get_some_strings(s):
    s=print("How many stirngs are in your set?")
get_some_strings(s)

    




