d={'madhav':1,'t':2}

try:
    for i,j in d.items():
        if d[i]==1:
            del d[i]

except:
    print(d)