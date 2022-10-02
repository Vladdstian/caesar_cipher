from alphabet import alphabet


def encrypt(message, shift):
    message_list = []
    coded_message = ""
    for letter in message:
        if letter in alphabet:
            index = alphabet.index(letter) + shift
            if index >= len(alphabet):
                index -= len(alphabet)
            message_list.append(alphabet[index])
        else:
            message_list.append(letter)
    for letter in message_list:
        coded_message += letter
    return coded_message


def decode(message, shift):
    message_list = []
    decoded_message = ""
    for letter in message:
        if letter in alphabet:
            index = alphabet.index(letter) - shift
            if index < 0:
                index += len(alphabet)
            message_list.append(alphabet[index])
        else:
            message_list.append(letter)
    for letter in message_list:
        decoded_message += letter
    return decoded_message
