c={
    
}
while True:
    print("\n1 Add item")
    print("2 Remove item")
    print("3 Show cart")
    print("4 Total items")
    print("5 Exit")
    ch=int(input("enter: "))
    if ch==1:
        i=input("enter:")
        q=int(input("enter:"))
        c[i]=c.get(i,0)+q
    elif ch==2:
        i=input("enter:")
        c.pop(i,None)
    elif ch==3:
        for k,v in c.items():
            print(k,":",v)
    elif ch==4:
        print(len(c))
    else:
        break
        