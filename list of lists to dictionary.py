l=[[1, 'Jean Castro', 'V'], [2, 'Lula Powell', 'V'], [3, 'Brian Howell', 'VI'], [4, 'Lynne Foster', 'VI'], [5, 'Zachary Simon', 'VII']]
i=0
d={}
for x in l:
    b=[]
    b=b+[x[1]]+[x[2]]
    d.update({x[0]:b})
    i=i+1
print(d)

