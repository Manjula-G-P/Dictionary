num = {'n1': [2, 3, 1], 'n2': [5, 1, 2], 'n3': [3, 2, 4]}
for i in num.keys():
    lis=num[i]
    n=0
    while n<len(lis):
        m=0
        while m<len(lis)-1:
            if lis[m]>lis[m+1]:
                lis[m],lis[m+1]=lis[m+1],lis[m]
            m=m+1
        n=n+1
    num[i]=lis
print(num)












        


