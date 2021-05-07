d=dict(x=list(range(11,20)),y=list(range(21,30)),z=list(range(31,40)))
print(d)
print(d["x"][4])
print(d["y"][4])
print(d["z"][4])
for i,j in d.items():
    print(i,"has value",j)