student_list = {'S  001': ['Math', 'Science'], 'S    002': ['Math', 'English']}
d={}
for i,j in student_list.items():
    a=i.split()
    c=a[0]+a[1]
    d.update({c:j})
print(d)

    
   