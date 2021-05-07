datas=[{"name":"komal","score":40,"school":"pyds"},{"name":"koma","score":40,"school":"pyd"},{"name":"jaya","score":60,"school":"pyds"},{"name":"sonam","score":60,"school":"union"},{"name":"Akshit","score":50,"school":"Summer Field school"}]
i=0
while i<len(datas):
    if datas[i]["school"]=="pyds" and datas[i]["score"]>=50:
        print(datas[i])
    i=i+1