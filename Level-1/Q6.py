num = int(input("Enter a number: "))

sum = 0

for i in range(1, num):
    if num % i == 0:
        sum += i
if sum == num and num > 0:
    print("Yes, it's a perfect number.")
else:
    print("No")