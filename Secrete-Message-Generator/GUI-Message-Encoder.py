import tkinter as tk

encoding_dict = {
    'A': '1', 'B': '2', 'C': '3', 'D': '4', 'E': '5', 'F': '6',
    'G': '7', 'H': '8', 'I': '9', 'J': '10', 'K': '11', 'L': '12',
    'M': '13', 'N': '14', 'O': '15', 'P': '16', 'Q': '17', 'R': '18',
    'S': '19', 'T': '20', 'U':'21', 'V': '22', 'W': '23', 'X': '24',
    'Y': '25', 'Z': '26'
}

def encode_message():
    message = entry_message.get()  # Getting the input from the text entry
    encoded_message = ''
    for char in message:
        if char.upper() in encoding_dict:
            encoded_message += encoding_dict[char.upper()]
        else:
            encoded_message += char
    label_encoded_message.config(text="Encoded Message: " + encoded_message)

# Creating the main window
window = tk.Tk()
window.title("Message Encoder")

# Creating the message input label and entry
label_message = tk.Label(window, text="Original Message:", font=("Arial", 12))
label_message.pack()
entry_message = tk.Entry(window, font=("Arial", 12))
entry_message.pack()

# Creating the Encode button
button_encode = tk.Button(window, text="Encode Message", command=encode_message, font=("Arial", 12))
button_encode.pack()

# Creating the encoded message label
label_encoded_message = tk.Label(window, font=("Arial", 12))
label_encoded_message.pack()

# Running the GUI event loop
window.mainloop()
