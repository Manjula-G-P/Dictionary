a="mississippi"
b=[]
i=0
k=0
d={}
while i<len(a):
    if a[i] not in b:
        b.append(a[i])
        j=i
        c=0
        while j<len(a):
            if b[k]==a[j]:
                c=c+1
            j=j+1
        d.update({a[i]:c})
        k=k+1
    i=i+1
print(d)