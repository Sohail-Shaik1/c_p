e={}
while True:
    print("\n 1.CREATE 2.DEPOSIT 3.WITHDRAW 4.TRANSFER 5.RICHEST 6.EXIT")
    c=int(input("enter your choice:  "))
    if c==1:
        an=int(input("enter accounr number:  "))
        n=input("enter name: ")
        b=float(input("enter initial balance:  "))
        e[an]={
            "name":n,
            "balance":b,
            "history":[]

        }
    elif c==2:
        an=int(input("enter accounr number:  "))
        if an in e:
            da=int(input("enter diposit amoount:  "))
            e[an]["balance"]+=da
        else:
            print("ivallid id")
    elif c==3:
        an=int(input("enter accounr number:  "))
        if an in e:
            
            wa=int(input("enter withdraw amount:  "))
            if  e[an]["balance"]>=wa:
                 e[an]["balance"]-=wa
            else:
                print("insufficient balnce:  ")

        else:
            print("invalid id")
    elif c==4:
        fn=int(input("enter from accounr number:  "))
        tn=int(input("enter  to accounr number:  "))
        ta=int(input("enter transfer ammount:  "))
        if e[fn]["balance"]>=ta:
            e[fn]["balance"]-=ta
            e[tn]["balance"]+=ta
        else:
            print("insufficient balance")
    elif c==5:
       r=max(e,key=lambda x: e[x]["balance"])
       print("richest person: ",e[r]["name"])
    elif c==6:
       print("exiting")
       break
    else:
       print("enter valid choice")

         
        
       
    
    
    
        
        
        
        
    
             

           

