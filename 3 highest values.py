my_dict={
    'a':50, 
    'b':58, 
    'c':56,
    'd':40, 
    'e':100, 
    'f':20,
    'h':150,
    'i':90
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
        max3=scendmax
    if maxnum>list1[j] and scendmax<max3:
        # max3=list1[j]
        max3=scendmax
    j+=1
print([maxnum,scendmax,max3])