## file1.py

from operator import  itemgetter
def my_fucn(my_list):

    my_list.sort(key=itemgetter('age'))
    print("Name of the Youngest employee:",my_list[0]['name'],'and','age:',my_list[0]['age'])



list = [{"name": "Tina", "age": 30, "birthday": "1990-03-10", "job": "Devops Engineer",
         "address": {"city": "New York", "country": "USA"}},
        {"name": "Tim", "age": 35, "birthday": "1985-02-21", "job": "Developer",
         "address": {"city": "Sydney", "country": "Australia"}},]
my_fucn(list)

## output ##
Name of the Youngest employee: Tina and age: 30





##file2.py
def string_fun(mystring):
   
    u_count=0
    l_count=0
    for i in mystring:
        if i.isupper():
            u_count+=1
            
        elif i.islower():
            l_count+=1
            
    print("The number of upper case letters:",u_count)
    print("The number of lower case letters:",l_count)
    
string=input("Enter any string:\n")
string_fun(string)


### output###
Enter any string:
Madhav
The number of upper case letters: 1
The number of lower case letters: 5


## file3.py
def list_fun(list):
    print("The elements that your are entered into list:",list)
    print("The even numbers are:\n")
    for i in list:
        if i%2==0:
            print(i)
            
            
my_list=list(map(int,input("enter elements into list:").strip().split(' ')))
list_fun(my_list)

### output ###

enter elements into list:1 2 3 4 5 6 7 8 9
The elements that your are entered into list: [1, 2, 3, 4, 5, 6, 7, 8, 9]
The even numbers are:

2
4
6
8





 ### MODULE ##
  
file4.py

from file1 import *
from file2 import  *
from file3 import  *


list=[{"name": "Tina", "age": 30, "birthday": "1990-03-10", "job": "Devops Engineer",
             "address": {"city": "New York", "country": "USA"}},
            {"name": "Tim", "age": 35, "birthday": "1985-02-21", "job": "Developer",
             "address": {"city": "Sydney", "country": "Australia"}},]
my_fucn(list)
mystring=input("Enter a string:\n")
string_fun(mystring)
my_list = [2,4,6,7]
list_fun(my_list)

## output ##

Name of the Youngest employee: Tina and age: 30
Enter a string:
Good Moring
The number of upper case letters: 2
The number of lower case letters: 8
The elements that your are entered into list: [2, 4, 6, 7]
The even numbers are:

2
4
6
