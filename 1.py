phone = input("Enter phone number: ")

if phone.isdigit() and len(phone) == 10:
    print("Valid phone number")
else:
    print("Invalid phone number")
