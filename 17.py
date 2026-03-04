s=input("enter: ")

d={}
for i in s:
    if i in d:
        d[i]=+1
    else:
        d[i]=1
print(d)
m=max(d,key=d.get)
print(m)