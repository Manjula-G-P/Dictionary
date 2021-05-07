d={1: ['Jean Castro'], 2: ['Lula Powell'], 3: ['Brian Howell'], 4: ['Lynne Foster'], 5: ['Zachary Simon']}
b=[]
d1={}
for i,j in d.items():
    d1.update({i:j[0]})
b.append(d1)
print(b)