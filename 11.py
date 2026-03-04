d={
    "sohail":90,
    "irfan":80,
    "king":70
}
d["srk"]=85
print(d)
t=max(d,key=d.get)

print("topper:",t,":",d[t])
avg=sum(i for i in d.values())/len(d)
print(avg)
