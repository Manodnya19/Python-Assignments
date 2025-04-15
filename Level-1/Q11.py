num = int(input("Enter a number: "))

def sum_of_digits(n):
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total

while num >= 10:
    num = sum_of_digits(num)
    print("Intermediate Sum:", num)

print("Final Output:", num)