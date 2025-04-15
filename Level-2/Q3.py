arr = [1, 2, 3, 4, 5]
k = 6
count = 0
seen = set()

for num in arr:
    target = k - num
    if target in seen:
        count += 1
    seen.add(num)
print("Pair count:", count)