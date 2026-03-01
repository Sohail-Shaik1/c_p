p=input("enter passsword: ")
e=[]
if len(p)<8:
    e.append(1)
if not any(c.isupper() for c in p):
    e.append(2)
if not any(c.islower() for c in p):
    e.append(3)
if not any(c.isdigit() for c in p):
    e.append(4)
s="!@#$%^&*()_+-="
if not any(c in s for c in p):
    e.append(6)
if not e:
    print("strong ppasswors")
else:
    print("weak ppassword")
    for i in e:
        print("-",e)

