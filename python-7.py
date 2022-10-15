class Person:
    def com_details(self,fname,lname,age):
        fname=fname
        lname=lname
        age=age


    def details(self,f,l):
        print("Full Name:",f,l)

class Student(Person):
    def lectures(self,l):
        for i in l:
            print(i)
    def operations(self,l):
        choice=input("if you want to add press y:").lower()
        if choice=='y':
            l1=list(map(str,input("add lectures!!:").split()))
            l=l+l1
            print("lectures after adding:\n")
            for i in l:
                print(i)
        choice2=input("if you want to remove any lecture press y:")
        if choice2=='y':
            l2=list(map(str,input("remove lectures here!!:").split()))
            for i in l2:
                l.remove(i)
            print("lectures after removing")
            for i in l:
                print(i)

p=Student()
print("*****STUDENT INFORAMTION*****")
c=int(input("enter how many students details u want to add:"))
for i in range(c):
    fname=input("enter student first name:")
    lname=input("enter student last name:")
    age=int(input("enter student age:"))
    p.com_details(fname,lname,age)

    p.details(fname,lname)
    l=list(map(str,input("enter lecctures he/she attend:\n").split()))
    p.lectures(l)
    p.operations(l)

class Proffessor(Person):
    def sub(self,s):
        print("list of subjcets:\n")
        for i in s:
            print(i)

    def operations(self,s):
        choice=input("if you want to add subjects press y").lower()
        if choice=='y':
            l1=list(map(str,input("add subjects:").split()))
            s=s+l1
            print("subjects after addded:\n")
            for i in s:
                print(i)

        choice2=input("if you want to remove press y:").lower()
        if choice2=='y':
            l2=list(map(str,input("remove subjects here:").split()))
            for i in l2:
                s.remove(i)
            print("subjects after removing:")
            for i in s:
                print(i)


pp=Proffessor()
print("*****PROFESSOR INFORAMTION*****")
fname=input("enter professor first name:")
lname=input("enter proffesor last name:")
name=fname+lname

age=int(input("enter proffesor age"))
pp.com_details(fname,lname,age)
pp.details(fname,lname)
s=list(map(str,input("enter subject").split()))

pp.sub(s)
pp.operations(s)

class Lecture(Proffessor):


    def get_lectures(self,name,max_stds,duration,list):
        name=name
        max_stds=max_stds
        duration=duration
        list=list

    def get_detailss(self,name,duration):
        print("Name of lecture:",name)
        print("Duration of lecture:",duration)

    def operations3(self,l):
        print("list of proffessors")
        for i in l:
            print(i)

        ch=input("if you want remove professor press y:")
        if ch=='y':
            ll=list(map(str,input("remove proffessors here:").split()))
            for i in ll:
                l.remove(i)
            print("after removing proffesors:\n")
            for i in l:
                print(i)



l=Lecture()
print("*****LECTURE INFORMATION*****")
c2=int(input("enter how many lecctures u want to add:"))
for i in range(c2):
    n=input("enter name of lecture:")
    max_std=int(input("enter no of stds attend:"))
    d=input("duration of class:")
    l.get_lectures(n,max_std,d,list)
    l.get_detailss(n,d)
    list=list(map(str,input("enter proffessor who gave this lecture:").split()))
    l.operations3(list)

print("END")





####OUTPUT#######


C:\Users\ADMIN\PycharmProjects\python1\venv\Scripts\python.exe C:/Users/ADMIN/PycharmProjects/python1/venv/classes.py 
*****STUDENT INFORAMTION*****
enter how many students details u want to add:2
enter student first name:Madhav
enter student last name:T
enter student age:22
Full Name: Madhav T
enter lecctures he/she attend:
aws python linux
aws
python
linux
if you want to add press y:y
add lectures!!:devops
lectures after adding:

aws
python
linux
devops
if you want to remove any lecture press y:y
remove lectures here!!:aws
lectures after removing
python
linux
devops
enter student first name:Kesva
enter student last name:M
enter student age:22
Full Name: Kesva M
enter lecctures he/she attend:
linux python
linux
python
if you want to add press y:y
add lectures!!:aws
lectures after adding:

linux
python
aws
if you want to remove any lecture press y:y
remove lectures here!!:linux
lectures after removing
python
aws
*****PROFESSOR INFORAMTION*****
enter professor first name:Manoj
enter proffesor last name:Reddy
enter proffesor age35
Full Name: Manoj Reddy
enter subjectpython
list of subjcets:

python
if you want to add subjects press yy
add subjects:aws devops
subjects after addded:

python
aws
devops
if you want to remove press y:y
remove subjects here:python
subjects after removing:
aws
devops
*****LECTURE INFORMATION*****
enter how many lecctures u want to add:1
enter name of lecture:devops
enter no of stds attend:20
duration of class:30 min
Name of lecture: devops
Duration of lecture: 30 min
enter proffessor who gave this lecture:Manoj
list of proffessors
Manoj
if you want remove professor press y:no
END

Process finished with exit code 0
