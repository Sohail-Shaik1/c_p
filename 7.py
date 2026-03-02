s=input("enter sentence:").lower().split()
f={}
le={}
for w in s:
    f[w]=f.get(w,0)+1
    l=len(w)
    if l not in le:
        le[l]=[]
        le[l].append(w)

h=max(s,key=len)

sh=min(s,key=len)
print("Word Frequency:", f)
print("Grouped by Length:", le)
print("Longest Word:", h)
print("Shortest Word:", sh)