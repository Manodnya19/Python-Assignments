def JtoI():
    try:
        with open("doc.txt", "r") as file:
            content = file.read()
            corrected_content = content.replace("J", "I")
            print("Corrected Content:\n")
            print(corrected_content)
    except FileNotFoundError:
        print("The file 'words.txt' was not found.")
JtoI()
