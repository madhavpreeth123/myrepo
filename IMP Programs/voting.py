
import random
from datetime import date
v_ids={}
l_id=[]
voted=[]

while True:
    user = input("If u are new user then press [y/n] for registraion:").lower()
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
            print("please note ur voter id:", num)
            print("By using ur id only u can .....")
            l_id.append(num)
            v_ids[name]=num


        else:
            print("Ur not eligible for vote...\n Note: only people eligible to vote above 18 years")




    else:
        break

list1=input("if you want to see register users press[Y/n]:")
if list1=='y':
    for i,j in v_ids.items():
        print(i,':',j)
if len(v_ids)>0:
    cand1=input("Enter 1st candidate name:")
    cand2=input("Enter 2nd candidate name:")

    cand1_count=0
    cand2_count=0
    while True:
        if len(l_id) > 0:
            id = int(input("Enter ur id:"))
            if id in l_id:
                l_id.remove(id)
                print(f"candidates are:\n1.{cand1}\n2.{cand2}")
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
    print("No user register yet!!!!")