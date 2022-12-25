arr1 = []
print("Enter 5 numbers ")
a = int(input("Enter Number 1: "))
b = int(input("Enter Number 2: "))
c = int(input("Enter Number 3: "))
d = int(input("Enter Number 4: "))
e = int(input("Enter Number 5: "))

arr1.append(a)
arr1.append(b)
arr1.append(c)
arr1.append(d)
arr1.append(e)

arr1.sort()

print(" The Min number is: ",  arr1[0])
print(" The Max number is: ",  arr1[4])





