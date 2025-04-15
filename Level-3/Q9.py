def run_length_encode(input_str):
    if not input_str:
        return ""

    encoded = ""
    count = 1

    for i in range(1, len(input_str)):
        if input_str[i] == input_str[i - 1]:
            count += 1
        else:
            encoded += input_str[i - 1] + str(count)
            count = 1


    encoded += input_str[-1] + str(count)
    return encoded

input_str = "wwwwaaadebbbbbw"
output = run_length_encode(input_str)
print(output)
