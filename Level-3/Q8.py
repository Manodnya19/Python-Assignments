def parse_encoded_string(encoded_str):
    
    parts = [part for part in encoded_str.split('0') if part]

    return {
        "first_name": parts[0],
        "last_name": parts[1],
        "id": parts[2]
    }

# Example usage
input_str = "Robert000Smith000123"
output = parse_encoded_string(input_str)
print(output)
