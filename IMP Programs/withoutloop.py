#printing elemts withou using loops
l=eval(input("enter list:"))
start=eval(input("enter start index:"))
end=eval(input("enter end index:"))
def my_fun(l,start,end):
    if start<0 or start>=end:
        return
    print(l[start])
    my_fun(l,start+1,end)

my_fun(l,start,end)

