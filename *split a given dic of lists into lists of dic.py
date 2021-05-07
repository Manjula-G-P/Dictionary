d={'Science': [88, 89, 62, 95], 'Language': [77, 78, 84, 80]}
b=[]
for v in d.values():
    b.append(v)
l=[]
i=0
while i<len(b[0]):
    j=0
    d1={}
    for k in d.keys():
        d1.update({k:b[j][i]})
        j=j+1
    l.append(d1)
    i=i+1
print(l)
    

