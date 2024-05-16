#C:\Users\sirik\PycharmProjects\HelloWorld\pythonProject\.venv
#source: https://www.youtube.com/watch?v=kqtD5dpn9C8&t=896s

# Python objects are immutable or cannot be changed.

#Variable Assignment
age=30
price=19.95

first_name = "Mosh"

is_online= False #boolean value

print(age)
print("Hello World!")
print(is_online)

#Exercise 1
patient_name='John Smith'
age=20
Is_new= True
print(patient_name)
print(age)
print(Is_new) #python is case sensitive

#Using input function in python
#input function always returns string
name= input("What is your name?")
print("My name is "+name) #concatenation

#Type conversion
birth_year= input("Enter your birth year: ")

age = 2024 - int(birth_year)
print(age)

# int(), float(), bool(), str() -> built in functions to convert datatypes

#Exercise 2
#print
#First: 10.1
#Second: 10
#Sum: 30.1
First = input("First: ")
Second= input("Second: ")
Sum= float(First) + int(Second)
print("Sum: ", Sum)

#Strings
course = "Python for beginners"
        #012345
print(course.upper())
print(course.lower())
print(course.find('y')) #returns 1
print(course.find('Python')) #returns 0

print(course.replace('for','4'))
print ('Python' in course ) #returns boolean

#Arithematic Operators
print(10/3) #returns 3
print(10//3) #returns 3.3333
print(10%3) #returns remainder
print(10**3) #10 to the power of 3

x=10
x=x+3
print(x)

x *= 3 #multiplication
print(x)

#multiplication and division have higher order, hence in the below case, first we multiply amnd then add
x = 10+3*2
print(x)

x = (10+3) *2
print(x)

#Comparision Operators
x = 3 >= 2
print(x)
# x = 3 < 2, x = 3!=2
#>,>=,<,<=,==,!=

#Logical Operators
#and, or, not
price = 5
print(price>10 and price<30)
print(price>10 or price<30)
print(not price>10)

#If statements
temperature = 25

if temperature > 30:
    print("It's a hot day")
    print("Drink plenty of water")
elif temperature>20:
    print("It's a nice day")
elif temperature >10:
    print("It's a bit cold")
else:
    print("It's cold")
print("Done")


#Exercise3
#input weight, input in kg or lbs, print weight in kg/lb based on users selection
weight = float(input("weight: "))
print("Weight is ", weight)
kg_lb= input("(K)g or (L)bs: ")
print(kg_lb)

if kg_lb=='k' or kg_lb=='K':
    print("Weight in Lb: ", weight * 2.205)
elif kg_lb=='L' or kg_lb=='l':
    print("Weight in Kg: ", weight / 2.205)


#to convert string to upper case: kg_lb.upper=='K'

#While loops
i = 1
while i <= 5:
    print(i)
    i = i+1

i = 1
while i <= 10:
    print(i * '*')
    i = i+1

#Lists  #012345
#
names = ['John','Siri', 'Bob','Mosh','Sam','Mary']
print(names)
print(names[1])

#excludes end index i.e 2
print(names[0:2])
print(names[-1])
print(names[:])
print(names[:-1])

names[0]='Jon'
print(names)
print(names[0:3])

#List Methods
#lists have a bunch of methods/functions
numbers = [1, 2, 3, 4, 5]
numbers.append(6)
print(numbers)

numbers.insert(0, -1)
print(numbers)

numbers.remove(3)
print(numbers)

numbers.clear()
print(numbers)

numbers = [1, 2, 3, 4, 5]
print(1 in numbers)
print(10 in numbers)

#to check number of items in the list
print(len(numbers))
print(" ")

#For Loops
numbers = [1, 2, 3, 4, 5]

for item in numbers:
    print(item )
print(" ")

i=0
while i< len(numbers):
    print(numbers[i])
    i=i+1
print(" ")

#Range function: used to generate sequence of numbers
numbers= range(0,5) #returns range object which stores sequence of numbers
for no in numbers:
    print(no) # prints 0 to 4
print(" ")

numbers= range(5,10) #returns range from 5 to 9
for no in numbers:
    print(no) # prints 0 to 4
print(" ")

numbers= range(5,10,2) #returns range from 5 to 9 with a step of 2
for no in numbers:
    print(no) # prints 0 to 4

#Tuples
#Tuples are immutable, i.e we cannot change them once we create them
numbers = (1, 2, 3, 3)
#numbers[0] =10 #throws error

#has only two methods: count and index
print(numbers.count(3))
print(numbers.index(1))
