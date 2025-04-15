arr = [1, 2, 3, 4, 5]
D = 2
D = D % len(arr)
rotated_arr = arr[-D:] + arr[:-D]


print("Array after rotation:", rotated_arr)