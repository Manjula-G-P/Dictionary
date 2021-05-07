d={"bijender":45,"deepak":60,"param":20,"anjili":30,"roshini":50}
lis=[]
for i in d.values():
    lis.append(i)
lis.sort()
lis.reverse()
d1={}
for i in lis:
    for k in d.keys():
        if d[k]==i:
            d1.update({k:i})
print(d1)

