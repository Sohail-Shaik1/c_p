d={}
n=int(input("enter nuber of students: "))
for i in range(n):
    n=input("n:")
    m=[]
    for i in range(5):
        ma=int(input("mar: "))
        m.append(ma)
    total=sum(m)
    avg=total/5
    if avg>=90:
        grade="A"
    elif avg>=70 and avg<=90:
        grade="B"
        
    else:
        grade="Fail"
    d[n]={
        "marks":m,
        "total":total,
        "avg":avg,
        "grade":grade
    }
topper=max(d,key=lambda x: d[x]["total"])
for k,v in d.items():
    print(k,v)
print("topper: ",topper)
