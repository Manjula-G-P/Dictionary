d=[
     {"first":"1"}, 
     {"second": "2"}, 
     {"third": "1"}, 
     {"four": "5"}, 
     {"five":"5"}, 
     {"six":"9"},
     {"seven":"7"}
]
d1=[]
i=0
while i<len(d):
    a=d[i]
    for x,y in a.items():
        if y not in d1:
            d1.append(y)
    i=i+1
print(d1)
        