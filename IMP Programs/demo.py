#n=5 (lenght of string)
#m=n-1
#s='abcde'
#t=['abcd','abcc','cddd','acde']   #out put: 2

def fucn(n,m,s,t):
    l1=[]
    count=0
    for i in s:
        l1.append(i)

    for i in range(len(l1)):
        c=l1.pop(i) #a
        for j in t:
            if "".join(l1)==j:
                count+=1
        l1.insert(i,c)
    print(count)


n=int(input("enter size of string:"))
m=n-1
s=input("enter a string:")
t=list(map(str,input(f"enter{m} elements into list").split()))
fucn(n,m,s,t)