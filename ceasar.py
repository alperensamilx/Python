  
def ceasar(direction ,text, shift):

        def encrypt(plain_text, shift_amount):
            cipher_text = ""
            for i in plain_text:
                postition = alphabet.index(i)
                new_position = postition + shift_amount
                new_letter = alphabet[new_position]
                cipher_text += new_letter
            print(f"The encoded is {cipher_text}")

        def decrypt(cipher_text, shift_amount):
            plain_text = ""
            for i in cipher_text:
                postition = alphabet.index(i)
                new_position = postition - shift_amount
                new_letter = alphabet[new_position]
                plain_text += new_letter
            print(f"The decoded is {plain_text}")

        if direction == "encode":
            encrypt(text, shift)
        elif direction == "decode":
            decrypt(text, shift)


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z''a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y','z']

should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26
    ceasar(direction, text, shift)

    result = input("Type 'yes' if you want to go again. Otherwise type 'no'.")
    if result =="no":
        should_continue = False
        print("Goodbye")

