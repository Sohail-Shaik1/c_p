n=int(input(" enter: "))
p=True
if n<2:
    print("mot a pprime")
for i in range(2,int(n**0.5)+1):
    if n%i==0:
        p=False
        break
if p:
    print("prime")
else:
    print("not a prime")
