import array as arr
a_list = [2,5,62,5,42,52,48,5]
a_array = arr.array('i',a_list)
print(a_array[2:5])
print(a_array[:-5])
print(a_array[5:])
print(a_array[:])
