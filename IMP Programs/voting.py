
import random
from datetime import date
try:
    v_ids={}
    l_id=[]
    voted=[]
    print("Welcome To Voting App".center(60,' '))
    print("___________________________________________")
    nu=int(input("Enter how many users u want to create:"))

    for i in range(0,nu):
            user = input("If u want to create a new user then press [y/n] :").lower()
            if user=='y':
                name=input("Enter ur name:")
                year=int(input("Enter birth of year[YYYY]:"))
                month=int(input("Enter ur mont[DD]:"))
                day=int(input("Enter day:"))
                bod=date(year,month,day)
                today=date.today()
                age=today.year-bod.year-((today.month,today.day)<(bod.month,bod.day))
                if age>18:
                    num = random.randint(100, 1000)
                    print("please note user voter id:", num)
                    print("By using ur id only user can vote .....")
                    l_id.append(num)
                    v_ids[name]=num


                else:
                    print("Ur not eligible for vote...\n Note: only people eligible to vote above 18 years")


    if len(l_id)>0:
        list1 = input("if you want to see created  users press[Y/n]:")
        if list1 == 'y':
            for i, j in v_ids.items():
                print(i, ':', j)

        print("Voting Process Started.....")
        print("Rules:\n This app is for only Two candiadtes \n By entering their names only the actual voting process will be start..")
    if len(l_id)>0:
                cand1=input("Enter 1st candidate name:")
                cand2=input("Enter 2nd candidate name:")
                print(f"candidates are:\n1.{cand1}\n2.{cand2}")

    cand1_count=0
    cand2_count=0

    if len(l_id)>0:
        while True:
            if len(l_id) > 0:

                    id = int(input("Enter user id:"))
                    if id in l_id:
                        l_id.remove(id)

                        choice = int(input("Vote for candidate choose either 1 0r 2:"))

                        if choice == 1:
                            cand1_count = cand1_count + 1
                            voted.append(id)
                            print("Successfully voted....")

                        elif choice == 2:
                            cand2_count += 1
                            voted.append(id)
                            print("Successfully voted...")

                        else:
                            print("OOPS!!! Wrong choice")

                    elif id in voted:
                        print("your are already voted!!")

                    else:
                        print("wrong id")

            else:
                    print("voting completed\n")
                    if cand1_count > cand2_count:
                        print(f"Winner is {cand1} with {cand1_count} votes....")
                        break
                    elif cand1_count < cand2_count:
                        print(f"Winner is {cand2} with {cand2_count} votes....")
                        break
                    elif cand1_count == cand2_count:
                        print("match tied...")
                        break

    else:
        print("No users Found!!!!1")
except:
    print("Enter details correctly")



    ### out put ####
    
    
    Enter how many users u want to create:4
If u want to create a new user then press [y/n] :y
Enter ur name:madhav
Enter birth of year[YYYY]:2000
Enter ur mont[DD]:4
Enter day:14
please note user voter id: 533
By using ur id only user can vote .....
If u want to create a new user then press [y/n] :y
Enter ur name:kesava
Enter birth of year[YYYY]:2004
Enter ur mont[DD]:2
Enter day:3
Ur not eligible for vote...
 Note: only people eligible to vote above 18 years
If u want to create a new user then press [y/n] :y
Enter ur name:sai
Enter birth of year[YYYY]:2002
Enter ur mont[DD]:2
Enter day:7
please note user voter id: 858
By using ur id only user can vote .....
If u want to create a new user then press [y/n] :y
Enter ur name:ashok
Enter birth of year[YYYY]:1999
Enter ur mont[DD]:12
Enter day:1
please note user voter id: 223
By using ur id only user can vote .....
if you want to see created  users press[Y/n]:y
madhav : 533
sai : 858
ashok : 223
Voting Process Started.....
Rules:
 This app is for only Two candiadtes 
 By entering their names only the actual voting process will be start..
Enter 1st candidate name:Jagan
Enter 2nd candidate name:Ka Paul
candidates are:
1.Jagan
2.Ka Paul
Enter user id:533
Vote for candidate choose either 1 0r 2:1
Successfully voted....
Enter user id:533
your are already voted!!
Enter user id:223
Vote for candidate choose either 1 0r 2:1
Successfully voted....
Enter user id:585
wrong id
Enter user id:858
Vote for candidate choose either 1 0r 2:1
Successfully voted....
voting completed

Winner is Jagan with 3 votes....
