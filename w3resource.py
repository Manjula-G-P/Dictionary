d='w3resource'
i=0
k=0
b=[]
d1={}
while i<len(d):
    if d[i] not in b:
        b.append(d[i])
        j=0
        c=0
        while j<len(d):
            if b[k]==d[j]:
                c=c+1
            j=j+1
        d1.update({d[i]:c})
        k=k+1
    i=i+1
print(d1)
        