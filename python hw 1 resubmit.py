#hw 1

#2: programming exercise 1
#a and b
print("Hello, world!")
print("Hello", "world!")
#in the first line, the comma is included in the pronted text as it is included in the quotes. the second line prints "Hello" then adds "world!" next
#c and d
print(3)
print(3.0)
#the first prints an integer, the second prints a float
#e,f, and g
print(2+3)
print(2.0 +3.0)
print("2"+"3")
#the first adds to integers, the second adds two floats, the third just print the two numbers next to each other
#i and j
print(2*3)
print(2**3)
#the first multiplies the integers, the second raises the 2 to the third power
#k and extra
print(7/3)
print(2//3)
#the first divides the first integer by the second, the second also divided the first integer form the second, but rounds down the remainder

print()
print()

#3: programming exercise 5
# can do: import chaos2.py or rewrite it:
# File: chaos. py 
# A simple program illustrating chaotic behavior. 
def main(): 
    print("This program illustrates a chaotic function")
    n=eval(input("How many numbers should I print?: "))
    x = eval(input("Enter a number between 0 and 1: ")) 
    for i in range(n):
        x= 3.9*x*(1-x) 
        print(x)
main()


print()
print()


#4: programming exercise 10
def kilometer():
    k=eval(input("kilometers to be converted: "))
    kilo=(k*0.62)
    print(kilo)
kilometer()

print()
print()

#5 exercise 5 from How to Think Like a Computer Scientist
def comp_int():
    p=10000
    n=12
    r=.08
    t=eval(input("number of years: "))
    A=p*(1+(r/n))**(n*t)
    print("final amount: ",A)
comp_int()








