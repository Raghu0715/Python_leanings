#CLASSES AND OBJECTS
#why we are creating the classes and objects

#How to create a class
#Use the keyword "class"

"""class customers:
    pass
x="hello"
c1=customers()
print()"""


#What is __main__?
# is nothing but from which file the class it is coming from

"""Attributes:- these are 2 types
1. class attribute:- come from class and these attributes accessible by every object(common attriutes)
2. object attribute:-means unique attributes that can be applicable to particular object"""

#create a class
"""class customer:
#create class attributes---> creating variables inside the class
    bank_name= "hfc Bank"
    branch = "mumbai"
    state = "maharasta"
    ifsc = "hfc000023"
#create a object
c1 = customer()
c2 = customer()
#how can an object can access the class attribute
print(c1.bank_name)
print(c2.ifsc)"""

#Create the methods for class customers
#What is methods
#methods can be created inside the class.
#methods are nothing but creating function the classes.


class Customer:
    # Create class attributes----> Creating variables inside the class
    bank_name = "HFC Bank"
    branch = "Mumbai"
    state = "Maharashtra"
    ifsc = "HFC000023"

    # Initialize the object attributes inside the class
    def __init__(self, name, age, initial_amount, account_num):
        """When you create an object, the __init__ method runs by default. It is an initialization method."""
        self.name = name
        self.age = age
        self.initial_amount = initial_amount
        self.account_num = account_num

    # Creating the methods
    def welcome(self):
        print(f"Hello {self.name} and welcome to {self.bank_name}, {self.branch}")

    def check_balance(self):
        print(f'Your current balance is {self.initial_amount}')

    def deposit(self, amount):
        self.initial_amount += amount
        print(f"Transaction is completed. "
              f"{amount} has been credited to your {self.account_num}. "
              f"The updated balance is {self.initial_amount}")

    def withdraw(self, amount):
        if amount <= self.initial_amount:
            self.initial_amount -= amount
            print(f"Transaction is completed. "
                  f"{amount} has been debited from your {self.account_num}. "
                  f"The updated balance is {self.initial_amount}")
        else:
            print("Insufficient balance")
            self.check_balance()

# Create an object
c1 = Customer(name="Python", age=28, initial_amount=10000, account_num=23858642)
c2 = Customer(name="raghu", age=22, initial_amount=10000, account_num=12345886)
# Access the particular methods
c1.welcome()
c1.check_balance()
c1.deposit(10000)
c1.withdraw(200000)

c2.welcome()
c2.check_balance()
c2.deposit(1000)
c2.withdraw(20000)
# Access class attributes
#print(c1.bank_name)
#print(c1.ifsc)

# Access object attributes
#print(c1.initial_amount)

#What is self
#it is a extra parameter in the method definition
#class.method(object())
#self acts a pointer/reference to access the object

"""__init__ Method: Initializes a new object's attributes.
self Keyword: Refers to the current object instance, allowing access to its attributes and methods."""

#step1--->create a class --->customer--->bank
#step2--->created a object by using variables for
#step3--->creating class attributes inside the class---> these are common attributes
#step4--->how to access class attributes by particular object--->print(c1.bank_name)
#step5--->created methods inside the class which are nothing but functions inside class
"""ex:- welcom(),check-balance(),deposit(),withdraw()"""
#step6---> how to access perticular method by particular object---> c1.welcome(),c1.deposit()


#Class
#Objects
#Methods
#INheritence:- the child object can acquire all the properties and behaviour of the parent object
#Data Abstraction:- data abstraction and encapsulation botha are like synonyms
#Polymorphism:- One task can be performed in many ways
#Encapsulation:-