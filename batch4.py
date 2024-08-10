#Functions:
""" Create a sum() function it can take 2 arguments to do a sum"""
"""def sum(a, b):
    print(a+b)

a=int(input("Enter your number: "))
b=int(input("Enter your number: "))
sum(a, b)"""

#write a python function to sum all the numbers in a list
#sample list: [8,2,3,0,7]
#expected output:20
"""def sum(numbers):
    total = 0
    for i in numbers:
        total=total +i
    print(total)
numbers =[8,2,3,0,7]
sum(numbers)"""

#write a function to multiply all the elements
"""def sum(numbers):
    total = 1
    for i in numbers:
        total=total *i
    print(total)
numbers =[1,2,3,4]
sum(numbers)"""

#write a python function to print  even numbers from given list
#sample list= [1,2,3,4,5,6,7,8,9]
#output=[2,4,6,8]
"""def even(num):
    for i in num:
        if i%2==0:
            print(i, end=" ")
num=[1,2,3,4,5,6,7,8,9]
even(num)"""

#write a function that converts the decimal num into binary num
"""def dectobin(num):
    if num>1:
        dectobin(num//2)
    print(num%2, end="")
dectobin(11)"""

#return()
"""def dectobin(num):
    if num>1:
        dectobin(num//2)
    return(num%2)
print(dectobin(11))"""

#Return:- return is a special keyword that can be use inside a function or method to send the fuction results back to the caller
"""sum=10
def f1(x):
    return(x+sum)
print(f1(5))"""

"""def f1(x):
    print(x)
f1(10)"""

"""def f2(x):
   return(x)
print(f2(10))"""

#what is the purpose of return?
""" when you return the value you can decide what you gonna do with value"""
"""x=len(input("Enter the string"))
print(x**2)"""

"""def f1(x):
    print(x) #---?10
print(f1(10)) # -----> None"""
#why we are getting none?
"""when i use print(x) and given the argument f1(10) the 10 will gets to the f1(x) place and first prints the 10 """

"""def f1(x):
    return x
print(f1(10))"""

"""sum=10
def fun_sum(x):
    return x+sum
print(fun_sum(100))"""

"""sum=0
def fun_sum(x):
    a= x+sum
print(fun_sum(100))"""

#write a program to print sum of range of numbers
#sample input=7
#expected output=28

"""n=int(input("Enter a number"))
sum=0
for i in range(0,n+1):
    sum+=i
print(sum)"""

"""n = int(input("Enter a number: "))
sum = sum(range(1, n + 1))
print(sum)"""

#List comprehension
#it offers you a smaller line of code and you can create a new list from the existing list
#print the fruits with letter A in it and store it in the new list
"""list_fruits=["Apple", "banana", "pineapple", "mango", "kiwi"]
new_list=[]
for i in list_fruits:
    if "A" in i:
        new_list.append(i)
print(new_list)"""

"""list_fruits=["Apple", "banana", "pineapple", "mango", "kiwi"]
#newlist=[items(i) for items(i) in "collection name")
new_list=[x for x in list_fruits if "e" in x]
print(new_list)"""

#print the new list without banana from the existing list_fruits
"""list_fruits=["Apple", "banana", "pineapple", "mango", "kiwi"]
new_list=[x for x in list_fruits if x != "banana"]
print(new_list)"""

#create the  numbers from 0 to 20
"""numbers=[]
for i in range(21):
    numbers.append(i)
print(numbers)"""

"""numbers=[i for i in range(21)]
print(numbers)

numbers=[i for i in range(21) if i%2==0]
print(numbers)

numbers=[i for i in range(21) if i%2!=0]
print(numbers) 
#Note so LC can offer shorter syntax and also time efficient"""

#create a new list of numbers in the range of 20 the output must be in multiples of 2
#Note syntax = new+list=[items (i) in items(i) in collection name]
"""num=[i*2 for i in range(21)]
print(num)"""



lambda
#what is lambda
#lambda is "Anonymous function"
#Anonymous function means this function does not have a name
"""def f1(X):
    return(X)
print(f1(10))"""

#Syntax for lambda():-"Lambda arguments:expression"
#so lambda is an expression function it can have many arguments and single expression
#Expression is kind og statement/ calculation/step using that values to give single
#lambda is an anonymous function how can you call it
# we generally use this function which have name
#means we can create a variable to call this function
"""x=lambda a:a+10
#where are you calling the lambda function use the variable name
print(x(5))"""

#lambda
#x=lambda a,b,c:a+b+c
#print(x(5,6,7))
#when we can use a lambda function
#create a function that can give sqaure of every number?
"""def square(x):
    return x**2
def cube(x):
    return x**3
def four(x):
    return x**4
def sqrt(x):
    return x**0.5
print(square(4))
print(cube(4))
print(four(4))
print(sqrt(4))"""

"""def power(n):
    return lambda a: a ** n
square =power(2)
cube =power(3)
print(square(6))
print(cube(2))"""

#similarly try the lambda function for the multiplication

#global variable and local varaible
#what is global variable
#the variable that can create outside the function
"""You can access the global variable inside a function where you can directly read its value.
To modify a global variable inside a function, you need to use the global keyword.
You can access the global variable outside the function anywhere in the code."""
#local variales is the peremenant variable
x="amazing"
"""def f():
    return x
print(f())"""

#what is local variable
# creating the variable inside the function is known as local variable
#local variales is the temporary variable ut only losts only inside the function
"""def f():
    x="fantastic"
    return x
print(f())"""
#NOte :- even the variables names are same the local variale never effect the global variale

#MAP():-
#what map does ?
# it use a function on
#what are iteratables
#iteratables  are list, tuples,sets array
#map will take an function and iterables.
"""Functions are the first class objects which means one fun can act as argument for another function"""

#Syntax:- Map=(function, iterables)
"""a=['apples', 'banana', 'cherries', 'pineapple']
length=[]
for i in a:
    length.append(len(i))
print(length)
l1=[len(i) for i in a]
print(l1)"""

a=['apples', 'banana', 'cherries', 'pineapple']
# if you want to display the output by using th map function we need decide in which iterables the output has to be
"""length=tuple(map(len,a))
length=list(map(len,a))
print(length)"""

"""def f1(x):
    return "hello "+x
print(f1("apples"))

#apply the function for rach item in the collection
l=list(map(f1,a))
print(l)"""

#when we have to use the map function?
#when we are having multiple user input then we can use the map function

"""user=input()
print(user)
print(type(user))"""
# i want to separate this value

"""user=input().split()
print(user)
print(type(user))"""
#how to convert above thing in interger
"""number=[]
for c in number:
    number.append(int(c))
print(number)
print(type(number))"""

#user.input().split()
"""number=tuple(map(int,input().split()))
print(number)"""


"""user=input().split()
print(user)
print(type(user))"""
#how to convert a list of interger into string
"""user=input().split()
print(user)
print(type(user))
number=[]
for x in user:
    number.append(int(x))
print(number)
print(type(number))"""


#user=input().split()
"""number = tuple(map(int,input().split()))
print(number)"""

#NOte :- before executing the map function you need to decide in what type of collection do we need to the output

#how can we ptint the following 10 20 30 40 50 in double that to in tuple
#Lambda:- you can have the multiple arguments awith single expression
"""double=tuple(map(lambda x : x*2, map(int,input().split())))
print(double)"""

"""map(lambda a : a*2, map(int,input().split()))
print(double)"""
#map(int,input().split())---> map storing entire thing /data, if we want it in a readable object to need to add "tuple", "list", "set"
#===========================================================================================================
"""filter()-----> collection_name(filter(function, iterable)) 
filter gives output of the collection if the condition is true"""
age=[18,40,26,31,24,56,16,22]
"""def adult(x):
    if x>=18:
        return x
f1=list(filter(adult,age))
print(f1)"""

"""f1=list(filter(lambda a: a>=18, age))
print(f1)"""
"""map() is used to apply a given function to each element of an iterable and returns
 a new iterable with the results. filter() is used to filter elements from an iterable 
 based on a given condition or function and returns a new iterable with the filtered elements."""


#how can i give more expression when iam using the conditional statements
#shall we use logical operators in lambda-----> yes we can use
"""f1=list(filter(lambda a:18<=a<=30, age))
print(f1)"""
"""so filter is basically your original collections that returns to or flase, 
any value that comes to be true the original value can be stored
 as a collection(list,set,tuples) of items."""
#LIst comphersion
#Lambda
#map()
#Filter() along with sending one fun as a argument to another fun

#Regular expression:- is a bult in package which isknown as "re"
#A RegEx, or regular expression  is a sequence of characetrs that forms a shorter
"""import re
txt ="hello world!"
#search whether s present in txt
x=re.search("world!$",txt)
print(x)"""
#REgular expressin function
#1.findall()--? return a list containing all matches
#search()--->returns match obj
#split()---->returns a list
#sub---->replace one or many matches with the string

#CLASSES AND OBJECTS
#why we ae creating the classes and objects

#HOw to cfreate a class
#Use the keyword "class"

"""class customers:
    pass
x="hello"
c1=customers()
print()"""


#What is __main__?
# is nothing nut from which file the class it is coming from

"""Attributes:- these are 2 types
1. class attribute:- come from class and these attributes accessible by every object(common attriutes)
2. object attribute:-means unqiue attributes that can be applicable to particular object"""

#create a class
"""class customer:
#create class attributes---> creating variables inside the class
    bank_name= "hfc Bank"
    branch = "mumbai"
    state = "maharasta"
    ifsc = "hfc000023"
#create a object
c1 = customer()
c2= customer()
#how can an object can access the class attribute
print(c1.bank_name)
print(c2.ifsc)"""

#Create the methods for class customers
#What is methods
#methods can be created inside the class.
#methods are nothing but creating function the classes.

class customer:
#create class attributes---> creating variables inside the class
    bank_name= "hfc Bank"
    branch = "mumbai"
    state = "maharasta"
    ifsc = "hfc000023"
    #Creating the methods
    def welcome(self):
        print("hello and welcome to hfc bank")

#create a object
c1 = customer()
c2= customer()
#how can we access the particular methods
c1.welcome()
c2.welcome()

#how can an object can access the class attribute
print(c1.bank_name)
print(c2.ifsc)

#What is self
#it is a extra parameter in the method definition
#class.method(object())
#self acts a pointer/reference to access the object











