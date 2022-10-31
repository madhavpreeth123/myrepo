#input= 50   ..>110010
#output= 13  ..>001101    1=1*2**0,0=0*2**1,....

def binary(num):
    n=bin(num)
    n=n[2:len(n)]
    res=''
    print(n)

    for i in n:
        if i=='0':
            res+='1'
        else:
            res+='0'
    print(res)
    sum=0
    '''res=res[::-1]
    for i in range(0,len(res)):
        sum+=(int(res[i])*2**i)'''

    for i in range(0,len(res)):
        sum+=(int(res[i])*2**(len(res)-(i+1)))
    print(sum)







num=int(input("enter number:"))
binary(num)