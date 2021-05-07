dic={
    "ball":"red",
    "bat":4,
    "wickets":8,
    "ball":"green",
    "bat":3
    }
# d={}
# for key,val in dic.items():
#     if key not in d:
#         d[key]=val
# print(d)
d={}
for x,y in dic.items():
    if (x,y) not in d:
        d.update({x:y})
    
print(d)