my_dict = {
    'a':50, 
    'b':58,
    'c':56,
    'd':40,
    'e':100, 
    'f':20
    }
maxnum=0
scendmax=0
max3=0
list1=[]
for i in my_dict.values():
    list1.append(i)
j=0
while j<len(list1):
    if list1[j]>maxnum:
        scendmax=maxnum
        maxnum=list1[j]
    if maxnum>list1[j] and scendmax<list1[j]:
        # scendmax=max3
        scendmax=list1[j]
        if max3<scendmax and max3<maxnum:
            #max3=list1[j]
            max3=scendmax
    j+=1
lis=[]
for k in my_dict.keys():
    if my_dict[k]==maxnum:
        lis.insert(0,k)
    elif my_dict[k]==scendmax:
        lis.insert(1,k)
    elif my_dict[k]==max3:
        lis.insert(2,k)
print(lis)
