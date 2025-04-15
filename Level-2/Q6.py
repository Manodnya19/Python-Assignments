# Q18.py

def is_power_of_two(n):
    if n <= 0:
        return False
    if n == 1:
        return True
    if n % 2 != 0:
        return False
    return is_power_of_two(n // 2)


num = int(input("Enter a number: "))
if is_power_of_two(num):
    print("Yes, it's a power of two.")
else:
    print("No, it's not a power of two.")
