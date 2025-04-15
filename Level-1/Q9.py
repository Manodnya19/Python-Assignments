# input_list = [1, 2, 3, 2, 4, 1, 2, 4, 5]

n = int(input("Enter number of elements: "))
input_list = []
print("Enter elements: ")
for i in range(n):
    input_list.append(int(input()))


dict1 = {}
for item in input_list:
    if item in dict1:
        dict1[item] += 1
    else:
        dict1[item] = 1
print("Frequency count:", dict1)