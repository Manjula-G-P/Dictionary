d={}
i=1
while i<=5:
    j=1
    b=[]
    while j<=10:
        b.append(i*j)
        j=j+1
    d.update({i:b})
    i=i+1
print(d)