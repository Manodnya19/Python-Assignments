def find_median(number_list):
    sorted_list = sorted(number_list)
    n = len(sorted_list)

    if n == 0:
        return "List is empty."

    if n % 2 == 0:
        mid1 = sorted_list[n // 2 - 1]
        mid2 = sorted_list[n // 2]
        median = (mid1 + mid2) / 2
    else:
        median = sorted_list[n // 2]

    return median

number_list = [7, 2, 5, 12, 12, 3]
print("Median:", find_median(number_list))