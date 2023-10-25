#chapter 5 discussion problem 1
#c
s1=("spam")
print(s1[1])
#e
s2="ni!"
print(s1[2]+s2[:2])
#g
print(s1.upper())


#chapter 5 discussion problem 2
#a
s2="ni!"
print(s2[0:2].upper())
#d
print(s1)
#e
print(s1[0:2],s1[3])

#chapter 5 discussion problem 3
#b
for w in "Now is the winter of our discontent...".split():
    print(w)
#c
for w in "Mississippi".split("i"):
    print(w,end="")
#e
msg=""
for ch in "secret":
    msg=msg + chr(ord(ch)+1)
    print(msg)


#4
print("grades=",end="")
grades=("F","D","C","B","A")
print(grades[0]*60,end="")
print(grades[1]*10,end="")
print(grades[2]*10,end="")
print(grades[3]*10,end="")
print(grades[4]*10)


#5 chapter 5 programming exercise 3

def exams():
    grade=input("Score:")
    index=input(int(grade)/10)
    letter=("F","F","F","F","F","F","D","C","B","A","A")
    final= letter[int(index)]
    return(final)
exams()
for i in range(100):
    print(i,exams(i))

#6 programming exercise 4
def main():
    myString = input("Enter the phrase: ")
    myString.split()
    acronym = ""
    for i in myString.split:
        acronym = acronym + i[0].upper()
    print("The acronym is ",acronym + ".")
main()
    
#7 programming exercise 5            
def main(name, value=0):
    for letter in name:
        value+=int(letter, 36)-9
    print (value)
main(input("insert name:").lower())

