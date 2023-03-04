#write the programme  to print those elements which contains "a" letters
li=["ravi","sunil","Abhinav"]
mi=[]
m1=[]
for i in li:
    if "a" in i:
        mi.append(i)
    else:
        m1.append(i)
print(mi)
print(m1)
