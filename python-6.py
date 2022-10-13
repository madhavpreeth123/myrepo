import random
num=random.randrange(1,10)
count=1

while True:
    try:
        guess_num=int(input("Guess the number between 1 to 9:\n"))
 
    
        if guess_num < num:
            print("You have guessed too low!!!!")
            count+=1
        elif guess_num > num:
            print("you have guessed too high!!!!")
            count+=1
        elif guess_num==num:
            print("YOU WON")
            print("you have guessed the number in ",count,"attempts")
            break
    except:
        print("Enter only number")
        
