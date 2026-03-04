d={
    "ali":90,
    "sohail":80,
    "irfan":70
}
while True:
    print("\n1. Add Student")
    print("2. Display Students")
    print("3. Find Topper")
    print("4. Find Average")
    print("5. Exit")
    c=int(input("enter your choice: "))
    if c==1:
        name=input("enter name: ")
        m=int(input("enter marks: "))
        d[name]=m
    elif c==2:
        for k,v in d.items():
            print(k,":",v)
    elif c==3:
        t=max(d,key=d.get)
        print("topper of the   class is ",t)
    elif c==4:
        avg=sum(i for i in d.values())/len(d)
        print("avge:",avg)
    else:
        break