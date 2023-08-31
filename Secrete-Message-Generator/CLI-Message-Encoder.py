encoding_dict = {
    'A': '1', 'B': '2', 'C': '3', 'D': '4', 'E': '5', 'F': '6',
    'G': '7', 'H': '8', 'I': '9', 'J': '10', 'K': '11', 'L': '12',
    'M': '13', 'N': '14', 'O': '15', 'P': '16', 'Q': '17', 'R': '18',
    'S': '19', 'T': '20', 'U':'21', 'V': '22', 'W': '23', 'X': '24',
    'Y': '25', 'Z': '26'
}
# ----------------------------------------- #
def encode_message(message, encoding_dict):
    encoded_message = ''
    for char in message:
        if char.upper() in encoding_dict:
            encoded_message += encoding_dict[char.upper()]
        else:
            encoded_message += char
    return encoded_message

# -------------------------------------------------- #
message = "HELLO WORLD"
encoded_message = encode_message(message, encoding_dict)


print("Original Message:", message)
print("Encoded Message:", encoded_message)

