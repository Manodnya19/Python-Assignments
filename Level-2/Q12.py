username = input("Create a username: ")
while True:
    password = input("Create a password: ")
    retype = input("Re-type password: ")

    if password == retype:
        print("Account created successfully!\n")
        break
    else:
        print("Passwords do not match. Please try again.\n")

# Login Step
attempts = 3
while attempts > 0:
    login_user = input("Enter your username: ")
    login_pass = input("Enter your password: ")

    if login_user == username and login_pass == password:
        print("Login successful!")
        break
    else:
        attempts -= 1
        print(f"Incorrect credentials. Attempts left: {attempts}\n")

if attempts == 0:
    print("Too many failed attempts. Account locked.")