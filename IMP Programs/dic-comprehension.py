num=[1,2,3,4,5]
#{1:1,2:4,3:9,4:16,5:25}

'''di={}
for i in num:
    di[i]=i**2
print(di)'''
print({i:i**2 for i in num})

#ex-2:
str="cOding"
#{'C':(asci of c,asci ofC),'O':(asci of c,asci of C)...}#ord(character),ord(character.swapcase())
'''dic={}
for i in str:
    dic[i.upper()]=(ord(i),ord(i.swapcase()))

print(dic)'''
print({i.upper():(ord(i),ord(i.swapcase())) for i in str})

#set comprehension

l=[1,2,3,4,5]
print({i**2 for i in l})