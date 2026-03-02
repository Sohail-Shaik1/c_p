e={}
while True:
    print("1.ADD 2.REMOVE 3.UPDATE SALARY 4.HIGHEST SALARY 5.EXIT")
    c=int(input("enter yur choice:  "))
    if c==1:
        id=int(input("enter id : "))
        n=input("enter name: ")
        age=int(input("enter age: "))
        s=float(input("enter salary: "))
        d=input("enter department:  ")
        e[id]={
            "name":n,
            "age":age,
            "salary":s,
            "department":d
        }
    elif c==2:
        id=int(input("enter id : "))
        if id in e:
            e.pop(id,None)
        else:
            print("id is invallid")
    elif c==3:
        id=int(input("enter id : "))
        if id in e:
            ns=float(input("enter new salary:  "))
            e[id]["salary"]=ns
        else:
            print("invalid id")
    elif c==4:
        h=max(e,key=lambda x: e[x]["salary"])
        print("highet slary employee ",e[h])
    elif c==5:
        print("exiting")
        break
    else:
        print("enter valid number")
    print(e)


                
           

