dic1={1:10,2:20}
dic2={3:30,2:40}
dic3={5:50,6:60}
d={}
for x,y in dic1.items():
        for i,j in dic2.items():
                # for p,q in dic3.items():
                        if x==i:
                                a=y+j
                                d.update({i:a})
                                print(d)
                        d.update(dic1)
                        d.update(dic2)
                        d.update(dic3)



        