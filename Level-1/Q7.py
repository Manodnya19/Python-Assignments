string1 = input("Enter first string: ").lower()
string2 = input("Enter second string: ").lower()

if sorted(string1) == sorted(string2):
    print("True")
else:
    print("False")