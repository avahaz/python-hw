#hw 6
print("hw 6")

print()
print()

#1 ch 7 discussion problem 2
print("#1 ch 7 discussion problem 2")
#Try/except handling is similar to ordinary decision as they both fix errors within a code/function. However, once an error is found while usinig a try/excpet handling, the code immediately jumps to run the except clause. In an ordinary decision structure, the code will run through all the options first. 

print()
print()


#2 ch 7 programming exercise 3
print("#2 ch 7 programming exercise 3")
def grades():
    g=float(input("Enter grade: "))
    if g>=90:
        print("Your grade is an A!")
    elif 80<=g<=89:
        print("Your grade is an B!")
    elif 70<=g<=79:
        print("Your grade is an C!")
    elif 60<=g<=69:
        print("Your grade is an D!")
    elif g<60:
        print("Your grade is an F!")
grades()

print()
print()


#3 ch 7 programming exercise 7
def babysitting():
    SH=int(input("Enter start time hour: "))
    SM=int(input("Enter start time minutes: "))
    EH=int(input("Enter end time hour: "))
    EM=int(input("Enter end tie minutes: "))
    wage=2.50
    if (SH<21 and EH>21):
        hours=EH-21
        minutes=EM 
        time_minutes=60-SM
        time_hours=21-(SH+1)
        time_hours=time_hours*60
        time=time_hours+time_minutes
        wage=(wage/60)*time
        time=(hours*60)+minutes
        cost=wage+(1.75/60)*time
        print("Money made is $",cost)
    elif(SH>=21):
        time_hours=EH-(SH+1)
        time_minutes=(60-SM)+EM
        time=(time_hours*60)+time_minutes
        cost=(1.75/60)*(time)
        print("Money made is $",cost)
    elif(EH<=21):
        time_hours=EH-(SH+1)
        time_minutes=(60-SM)+EM
        time=(time_hours*60)+time_minutes
        cost=(wage/60)*time
        print("Money made is $",cost)
babysitting()     
        

print()
print()

#4 ch 7 programming exercise 8
print("#4 ch 7 programming exercise 8")
def congress():
    age=int(input("Enter age: "))
    cit=int(input("Enter years of citizenship: "))
    if age<25 or cit<7:
        print("Not eligible for the House or Senate")
    if 25<=age and 7<=cit:
        print("Eligible for House Rep")
    if 30<=age and 9<=cit:
        print("Eligible for Senator")
congress()

        
print()
print()


#5 edit a program from previous hw
print("#5 edit a program from previous hw")
    #6 ch3 programming exercise 7 *to be edited*
print("#6 ch3 programming exercise 7 *to be edited*")
def distance():
    x1=eval(input("enter the first x coordinate: "))
    y1=eval(input("enter the first y coordinate: "))
    x2=eval(input("enter the second x coordinate: "))
    y2=eval(input("enter the second y coordinate: "))
    from math import sqrt
    d=sqrt((x2-x1)**2+(y2-y1)**2)
    print("the distance between the points is: ",d)
print()
print("*edited program*")
#6 ch3 programming exercise 7
print("#6 ch3 programming exercise 7")
def distance():
    x1=eval(input("enter the first x coordinate: "))
    y1=eval(input("enter the first y coordinate: "))
    x2=eval(input("enter the second x coordinate: "))
    y2=eval(input("enter the second y coordinate: "))
    from math import sqrt
    d=sqrt((x2-x1)**2+(y2-y1)**2)
    if d==0:
        print("the distance between the points is: ",d)
    if d>0:
        print("the real distance is: ",d)
#the program outputs a square root number. 0 only has one singel sqrt which is 0, there is no positive or negative. Any other number the program could give, however, is the positive sqrt, technically leaving another solution. However, because the porblem deals with distance, tehre is no negative distance, giving the "real" distance as teh positive integer.
distance()







