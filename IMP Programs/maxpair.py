#l=[0,1,5,7,3,9]
#output= (7,9) ....> max pair

def max_pair(arr):
    if len(arr)<2:
        print("no pair exists")
        return
    else:
        a=arr[0]
        b=arr[1]
        for i in range(0,len(arr)):
            for j in range(i+1,len(arr)):
                if arr[i]*arr[j] >(a*b):
                    a=arr[i]
                    b=arr[j]
        return a,b


arr=eval(input("enter a list"))

print(max_pair(arr))