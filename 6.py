p={}
n=int(input("enter number of players: "))
for _ in range(n):
    na=input("enter player's name: ")
    s=list(map(int,input("enter scores separated by spce").split()))
    p[na]=s
st={}
for name,score in p.items():
    total=sum(score)
    avg=total/len(score)
    st[name]={"total":total,"avg":avg}
h=max(st,key=lambda x: st[x]["total"])
l=min(st,key=lambda x: st[x]["total"])
print("\n player statastics")
for k,v in st.items():
    print(k,":",v)

ov_a=sum(v["total"] for v in st.values())/n
print("overall average :",ov_a)
for k in st:
    if st[k]["total"]>ov_a:
        print(k)
