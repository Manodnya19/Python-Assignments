def get_even_length_words_from_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()

    result_lines = []
    for line in lines:
        words = line.strip().split()
        even_words = [word for word in words if len(word) % 2 == 0]
        result_lines.append(' '.join(even_words))

    return '\n'.join(result_lines)

output = get_even_length_words_from_file("doc.txt")
print("Filtered content:\n", output)
