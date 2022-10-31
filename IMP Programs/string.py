s="aaabbcccd"    ###out put: a3b2c3d
res=""
for i in s:
    if s.count(i)==1:
        res+=i
    if i not in res:
        c=s.count(i)
        res+=i+str(c)


print(res)
