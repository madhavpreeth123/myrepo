st1=input("enter a string:")
st1=st1.split()
n=int(input("enter a num:"))
d={}

for word in st1:
    if word not in d:
        d[word]=1 #d{'man':1}

    else:
        d[word]+=1 #d{'man':2}
for key in d:
    if d[key]==n:
        print(key,end=" ")



