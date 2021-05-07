i=0
d={}
while i<10:
    name=input("enter a name:")
    age=int(input("enter age:"))
    dic={name:age}
    d.update(dic)
    i=i+1
print(d)