i=1
d={}
while i<=15:
    j=i
    while j<=i:
        d.update({i:i*j})
        j=j+1
    i=i+1
print(d)
        

