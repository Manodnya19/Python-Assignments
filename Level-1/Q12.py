num = int(input("Enter a number: "))
revnum = 0

while num > 0:
    digit = num % 10
    revnum = revnum * 10 + digit
    num //= 10

print("Reversed number:", revnum)