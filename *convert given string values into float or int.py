l=[{'x': '10.12', 'y': '20.23', 'z': '30'}, {'p': '40.00', 'q': '50.19', 'r': '60.99'}]
i=0
while i<len(l):
    d=l[i]
    for k,v in d.items():
        f=float(v)
        d[k]=f
    i=i+1
print(l)
