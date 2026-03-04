e={

}
while True:
    print("\n1 Add Employee")
    print("2 Remove Employee")
    print("3 Find Highest Salary")
    print("4 Display Employees")
    print("5 Exit")
    c=int(input("enter: "))
    if c==1:
        id=int(input("enter id: "))
        n=input("enter name: ")
        s=int(input("enter salary: "))
        a=int(input("age: "))
        e[id]={"name":n,"age":a,"salary":s}
    elif c==2:
        id=int(input("enter id: "))
        e.pop(id,None)
    elif c==3:
        h=max(e,key=lambda x: e[x]["salary"])
        print("highest emloyee salary: ",e[h]["name"])
    elif c==4:
        for k,v in e.items():
            print(k,":",v)
    else:
        break
           

    
