inp = input("Enter a string: ")

letters = 0
digits = 0

for char in inp:
    if char.isalpha():
        letters += 1
    elif char.isdigit():
        digits += 1

# Print the result
print(f"Alphabets: {letters} & Number : {digits}")