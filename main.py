from morse_code_dict import morse_code_rules


def text_to_morse(text_to_be_encoded):
    encoded_output = []
    for str_txt in text_to_be_encoded.upper():
        if str_txt in morse_code_rules:
            encoded_output.append(morse_code_rules[str_txt])
        else:
            return f"The character {str_txt} is invalid."
    return f"The morse code code is {" ".join(encoded_output)}"


def morse_to_text(morse_to_be_decoded):
    list_morse = morse_to_be_decoded.split()
    decoded_output = ""

    for m in list_morse:
        if m in morse_code_rules.values():
            decoded_output += list(morse_code_rules.keys())[list(morse_code_rules.values()).index(m)]
        else:
            return f"The morse code {m} is invalid."
    return f"The text is {decoded_output}"


while True:
    user_input = input('Welcome to the Morse Code Converter. Press "e" to encode or press "d" to decode: ')

    if user_input.lower() == "e":
        input_text = input("Please enter the text to be encoded: ")
        print(text_to_morse(input_text))
        y_or_n = input('Press "x" to exit or press other key to keep using: ')
        print("")
        if y_or_n.lower() == "x":
            break

    elif user_input.lower() == "d":
        input_morse = input("Please enter the morse_code: ")
        print(morse_to_text(input_morse))
        y_or_n = input('Press "x" to exit or press other key to keep using: ')
        print("")
        if y_or_n.lower() == "x":
            break

    else:
        print("Invalid letter. Please try again...")
