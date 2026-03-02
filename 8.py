c=["A","B","C"]
v={i:0 for i in c}
v_u=set()
while True:
    u=input("enter usre name or done: ")
    if u=="done":
        print("exiting")
        break
    if u in v_u:
        print("user already voted")
        continue
    vote=input("vote for A OR B OR C")
    if vote in v:
        v[vote]+=1
        v_u.add(vote)
    else:

        print("invalid candidate")
print("final votes: ",v)
winner=max(v,key=v.get)
print("winner: ",winner)
