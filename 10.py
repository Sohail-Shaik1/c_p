d={}
s=input("enter: ")
w=s.split()
for i in w:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
print(d)
for i in d:
    print(i,":",d[i])