my_list = [10, 20, 30, 40, 50]

try:
    index = int(input("Enter an index to access an element: "))
    print(f"Element at index {index}: {my_list[index]}")
except IndexError:
    print("IndexError: The index is out of range.")
except ValueError:
    print("ValueError: Please enter a valid integer.")