lst = []
n = int(input("Number of elements:"))

for i in range(0,n):
    elem = input()

    lst.append(elem)
print("List:", lst)
mid=int(len(lst)/2)
print("The middle element is:", lst[mid])