import string

#get alphabet using the string module so we don't have to type it out by ourselves
alphabet = list(string.ascii_lowercase)

direction = ''

def encrypt(plain_text, shift_amt):
    encr_text = ""
    for letter in plain_text:

        position = alphabet.index(letter)
        new_position = ""

        # prevent out of range index
        if not (position + shift_amt > len(alphabet)):
            new_position = position + shift_amt
        else:
            new_position = (position + shift_amt) - len(alphabet)
        encr_text += alphabet[new_position]
    print("Encrypted text:")
    print(f"{encr_text}")

def decrypt(plain_text, shift_amt):
    dencr_text = ""
    for letter in plain_text:
        position = alphabet.index(letter)
        new_position = ""

        #prevent out of range index
        if not (position - shift_amt < 0):
            new_position = position - shift_amt
        else:
            new_position = (position - shift_amt) + len(alphabet)
        dencr_text += alphabet[new_position]
    print("Dencrypted text:")
    print(f"{dencr_text}")

while not (direction == 'encode') or (direction == 'decode'):
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")

text = input("Type the message you want to encode/decode:\n").lower()

shift = int(input("Type the shift number:\n"))

if direction == 'encode':
    encrypt(text,shift)
elif direction == 'decode':
    decrypt(text,shift)