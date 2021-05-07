x=['S001', 'S002', 'S003', 'S004']
y=['Adina Park', 'Leyton Marsh', 'Duncan Boyle', 'Saim Richards']
z=[85, 98, 89, 92]
n=0
d={}
for i in x:
    d1={}
    d1.update({y[n]:z[n]})
    d.update({i:d1})
    n=n+1
print([d])
    

