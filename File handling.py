#what is file handling?
#handling certain file which is not python file.
#pdf,xcel,json--etc
#to handle the file in python we require a inbuilt function whcih is "open function"
#while your handling the file we will be having 4 modes.
#Modes:- r, a, w, x
#x-mode--> it is used to create a new file.
#f = open('trail.txt', 'x')
#w- mode--> over write mode.
"""f = open('trail.txt','w')
f.write("i am applying write mode to my file,"
        "if i write one more time my content can be overwritten ")
f.close()"""
import xlrd

# r-->read mode--> to read the content in file
#by default when you use the open function it is in read mode.

# f = open('trail.txt','r')
# print(f.read())
# f.close()

#write mode:-
"""f = open("trail.txt",'w')
f.write("i am over writing my content in the file"
        "so the previous content can be over written")
f.close()"""

#a-Mode-->append mode
# f = open('trail.txt','a')
# f.write('i am adding extra content at end of the existing content')
# f.close()

#read the file.
"""f = open('trail.txt')
print(f.read())
f.close()"""

#================================================================================

#To read the excel file use "xlrd" library
#what is xlrd
"""xlrd is a library for reading data and formatting information from excel file.it supports only .xls format."""
"""loc = "C:\\Users\\HP\\OneDrive\\Desktop\\Documents\\Downloads\\Financial Sample (1).xls"
#use the xlrd.open_workbook to read the file
wb = xlrd.open_workbook(loc)
#how to access the particular sheet data
sheet = wb.sheet_by_index(0)
#read data cell wise
#i want to know how many rows and columns are there in given file
print(sheet.nrows)
print(sheet.ncols)
#read the particular cell
#cell_value(row, col)
#indexing can be starts from zero
print(sheet.cell_value(7, 2))
#print entire rows
print(sheet.row_values(0))
print(sheet.col_values(1))
#extract all the data in console
for x in range(sheet.nrows):
    print(sheet.row_values(x))"""

#ITERARORS:-
"""iterators helps you to take large bunch of data in limited memory space"""
#it breaks the large data into tiny chunks
#in iterators we have 2 protocols
#1. __iter__()
#2. __next__()
"""l = ["apple", "banana", "watermelon", "kiwi", "orange"]
for x in l:
    #x is iter over each and every element in collection
    print(x)
x=iter(l)
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))"""



"""class number:
    def __iter__(self):
        self.inital = 0
        return self
    def __next__(self):
        if self.inital <=5:
            x = self.inital
            self.inital +=1
            return x
        else:
            StopAsyncIteration("are you mad")
n = number()
#for x in n:
 #    print(x)
x = iter(n)
print(next(n))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))"""

#pip package
#pickling
#connecting with you mysql by using python
#python json
#practical examples on four pilers of opps.
#===========================================================================

#GENERATOR :-
#generator is  a function that returns an iterator and produce a sequence of values when iterated is over
#when we have to use the generators
"""generators are use when we want to produce large sequence of values,
but we dont want to store all of them in the memory at once."""

#use "def", instead of "return" use the "yield"
"""def my_generator(n):
    value = 0
    #loop until the counter is less than n
    while value < n:
        yield value
        value += 1  # value+1
    #iterator over your grneator to genrerate sequence of values
for value in my_generator(3):
    print(value)"""


""" NOTE:- when you are using integer directly 
 into for loop its throughs an error use it with 
 range function when your using generators then
  instead return use yield it support int object in for loop"""
#=============================================================================

#pickling:-
"""The process of converting any type of object in
to bytes in python
 for example (list, tuple, set-----et) on to bytes is known as pickling"""
"""When it comes to python this pickling conversions is
 known as "serialisation", "deserialization". """

#What is bytes?
#0's and 1's is known as bytes
#to do pickling use package called pickle

#conversion of 2d data format to 1d data and store it.serialisation
#and in same time conversion 1d data in to 2d data is known  as pickle (deserialization)


"""import pickle
#open a pickle file.txt
pickle_file = open("pickle2.txt", "wb")  #wb is known as work and bytes
#use pickle.dump to dump the file
my_dict = {'1': "a", "2": "b"}
pickle.dump(my_dict, pickle_file)
#pickle.dump(collection_name, pickle_file name(where you want to store this data)
#in the above you dump the data in to serialisation

#if you want to read to visualise the real datathen follow the
pickle_file = open("pickle2.txt", "rb")
#load the data that you have stored
new_dict = pickle.load(pickle_file)
print(new_dict)"""

#step1:-import pickle library
#step2:- creating a pickle file in "wb"
#step3:- use "pickle.dump" to convert the data
#step4:-read the  actual data bu using "open(pickle_filename", "rb")
#step5:- after that load the data into new_file
#step6:- print the file
#========================================================================


#Python pip--> python install packager
"""Pip is a package manager for Python packages, or modules, that is written in Python """

#What is package?
#package is basically something that contains all the files you needed.
#package contains all the files you need of certain modules

#What is module?
#modules are code libraries which you can include in your project
#Numpy
#Pandas
#matplotlib and seaborn
#Pendulum
#python image processing
#moviepy
#tkinter
#pyqt
#py32
#pytest

#how to install this package?
#what is global package and what is local package
#how to install this packages
#py -m pip install "Package name" when you use cmd.
#!pip install "package name"--->collab notebook and jupiter notebook

#what is global package and local package?
"""import camelcase
x=camelcase.CamelCase()
a="hi there! this is the message to check each word of letters are capatlized"
print(x.hump(a))"""

#How to unistall package from cmd?
#py -m unistall "package name"
#how to check what are all packages present in you system.
#pip list
#How to upgrade pip?
#python.exe -m pip install --upgrade pip
#python -m pip install --upgrade pip

#how to pip the versions of the pip
#py -m pip --version

#=============================================================
#JSON--- javascript object notation
# it is basically a syntax that for storing and exchanging data.
"""{"first_name" : "shahul",
    "last_name"   : "sk",
    address:{street:3rd bsnl office,
        "city" : hyd}"""

import json
#what is parse?
""" it is a method of data converted in to another from of a data"""

"""person ={"name":"andrew",
         "lamguages":["eng","french"]}
#convert this is to jason format
person_dict=json.dumps(person)
print(person_dict)
print(type(person_dict))"""

#lets open a json file "with open "
loc="C:\\Users\\HP\\OneDrive\\Desktop\\Documents\\Downloads\\sample1.json"
with open(loc) as f:
    data= json.load(f)
print(data)
print(type(data))

#Data structues
#Linked List
#trees
#arrays