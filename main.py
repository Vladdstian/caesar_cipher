from code_decode import decode, encrypt

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

if direction == "encode":
    print(f'Here is the encoded message "{encrypt(text, shift)}"')
else:
    print(f'Here is the decoded message "{decode(text, shift)}"')
