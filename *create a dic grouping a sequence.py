l=[('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
d={}
i=0
while i<len(l):
    b=[]
    j=0
    while j<len(l):
        if l[j][0]==l[i][0]:
            b.append(l[j][1])
        j=j+1
    d.update({l[i][0]:b})
    i=i+1
print(d)

