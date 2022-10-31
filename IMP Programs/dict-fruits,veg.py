d={'orange':'fruit','potato':'vegetable','banana':'fruit','onion':'vegatable'}
##{'fruits':[orange,banana],'vegetables':[potato,onion]}
d1={}
for i in d:
    if i not in d1:
        d1[i]=d[i]


