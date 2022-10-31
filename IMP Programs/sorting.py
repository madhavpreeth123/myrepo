#AB2C4
#ABC24
s=input("enter a string:")
alpa=[]
num=[]

for i in s:
    if i.isalpha():
        alpa.append(i)

    else:
        num.append(i)
output=sorted(alpa)+sorted(num)
print(''.join(output))
