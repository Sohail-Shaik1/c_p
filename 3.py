p={
    "rice":50,
    "milk":30,
    "bread":40,
    "oil":150
}
cart={}
total=0
while True:
    item=input("enter item or done: ")
    if item=="donerice":
        break
    if item in p:
        q=int(input("enter quntity: "))
        cart[item]=cart.get(item,0)+q
    else:
        print("item is not available")
for k,v in cart.items():
    total=p[k]*q+total
if total>1000:
    d=total*0.10
else:
    d=0
f=total-d
print("\ncart:",cart)
print("total: ",total)
print("discount: ",d)
print("total bill: ",f)