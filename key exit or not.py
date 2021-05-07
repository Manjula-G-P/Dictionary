dic={"name":"Raju","marks":56}
user=input("enter a key:")
if user in dic.keys():
    print(user,"is existed")
else:
    print(user,"not existed")