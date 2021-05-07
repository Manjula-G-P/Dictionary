d={'#FF0000': 'Red', '#800000': 'Maroon', '#FFFF00': 'Yellow', '#808000': 'Olive'}
c=0
for i in d.values():
    for j in i:
        c=c+1
print("total length of values:",c)