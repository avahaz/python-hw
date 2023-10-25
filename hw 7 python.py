#hw 7

print()

#1 ch8 discussion question 1
print("#1 ch8 discussion question 1")
#a)
#definite loops repeat someting a certain number of times. Indefinite loops repeat until acertain condition is met.
#b)
#for loops are good for a set umber of iterations. While loops are good for when the nuber of iterations is unknown.
#c)
#an interactive loop runs on demand and prompts the user. Sentinel loops run until they are prompted to stop by the user.
#d)
#sentinel loops use user interactions. End of file loops use imported files and return strings taht are used as sentinel values.


print()
print()


#2 ch8 discussion question 2 (all sub)
print("#2 ch8 discussion question 2 (all sub)")
#a)not (P and Q)
    #((not P) and (not Q))
#b)(not P) and Q
    #Q and (not P)
#c)(not P) or (not Q)
    #(not(P and Q)
#d)(P and Q) or R
    #(R or P) and (R or Q)
#e)(P or R) and (Q or R)
    #(R or (P and Q))

print()
print()


#3 ch8 discussion question 3 (ac)
#a)
def sum():
    sum = 0.0
    moredata="yes"
    while moredata == "yes":
        x=int(input("Enter the numbers: "))
        sum = sum + x
        moredata=input("Do you have more data? (yes or no)")
    print("the sum is", sum)
sum()
#c)
def sums():
    total= 0
    x=float(input("Enter a number, 999 to quit:"))
    while x!=999:
        total = total + x
        x = float(input("Enter a number, 999 to quit:"))
    print("\nThe sum is", total)
sums()


print()
print()


#4 ch8 programming exercise 1
print("#4 ch8 programming exercise 1")
def fib_seq():
    n=int(input("Enter nth term: "))
    a = 0
    b = 1
    if n < 0:
        print("Incorrect input")
    elif n == 0:
        return 0
    elif n == 1:
        return b
    else:
        for i in range(1, n):
            c = a + b
            a = b
            b = c
        return b
fib_seq()


print()
print()

#5 ch8 programmng exercise 4
print("#5 ch8 programmng exercise 4")
def syr(x):
    result=[x]
    while x != 1.0:
        if x%2==0.0:
            x=x/2
            result.append(int(x))
        else:
            x=3*x+1
            result.append(int(x))
    return result
def main():
    x=int(input("Enter positive starting value: "))
    if x <= 0:
        print("invalid input")
    sequence=syr(x)
    print(sequence)
main()


#6 Git


