import array as arr

a = arr.array('i', [2, 4, 6, 8])
print("First Element:", a[0])
print("Last Element:", a[-1])

a.append(10)
print(a)

a[1] = 40
a[3] = 80
print(a)

x = len(a)
print(x)

a.extend([12,14,16])
print(a)

b_list = [1,2,3,4,5,6]
b_array = arr.array('i',b_list)
print(b_array[2:5])
print(b_array[:-5])
print(b_array[5:])
print(b_array[:])

x = len(b_array)
for x in b_array:
    print(x)