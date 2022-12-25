name = input("Enter your name:  ")
age = input("Enter your age:  ")
address = input("Enter your address:  ")

if name == "" or age == "" or address == "":
    print("One of your inputs is empty")

if name.isdigit() or type(age) != int or address.isdigit():
    print("One of your inputs has invalid type")

else:
    print(f"Hello Mr./Miss: {name} age  {age}  of  {address}  thanks for being one of our community ... enjoy")
