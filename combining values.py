d={'1':['a','b'], '2':['c','d']}
lis=[]
for i in d.values():
    lis.append(i)
i=0
while i<len(lis):
    j=0
    while j<=1:
        print(lis[0][i],end="")
        print(lis[1][j])
        j=j+1
    i=i+1  