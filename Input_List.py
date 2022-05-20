lst = []
n = int(input("Number of Element:"))

for i in range(0,n):
    elem = input()

    lst.append(elem)

print("The last element is:", lst[-1])