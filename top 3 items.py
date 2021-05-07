d={'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55, 'item5': 24}
val=[]
for i in d.values():
    val.append(i)
print(val)
maxnum=0
smax=0
tmax=0
i=0
while i<len(val):
    if val[i]>maxnum:
        maxnum=val[i]
        smax=maxnum
    if maxnum>val[i] and smax<val[i]:
        smax=tmax
        smax=val[i]
        if tmax<smax and tmax<maxnum:
            tmax=val[i]
            tmax=smax


    i=i+1
print(maxnum,smax,tmax)
