dic =  {
   'Alex': ['subj1', 'subj2', 'subj3'], 
   'David': ['subj1', 'subj2']}
c=0
for x,y in dic.items():
    for i in y:
        c=c+1
print("total values count:",c)
