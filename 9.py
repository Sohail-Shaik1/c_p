n=int(input("enter num: "))
p=True
if n<2:
    print("not prime")
for i in range(2,int(n**0.5)+1):
    if n%i==0:
        p=False
        break
if p==True:
    print("Prime")
else:
    print("not a prime")


