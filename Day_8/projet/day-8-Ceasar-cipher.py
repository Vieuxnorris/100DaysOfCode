from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

lenAlphabet = len(alphabet) - 1
userRetry = True

# def encrypt(text, shift):
#     textEncrypter = ""
#     for letter in text:
#         indexAlphabet = alphabet.index(letter) + shift

#         if indexAlphabet > lenAlphabet:
#             indexAlphabet -= (lenAlphabet + 1)

#         textEncrypter += alphabet[indexAlphabet]

#     print(textEncrypter)

# def decrypt(text, shift):
#     textDecrypt = ""
#     for letter in text:
#         indexAlphabet = alphabet.index(letter) - shift

#         if indexAlphabet < 0:
#             indexAlphabet += (lenAlphabet + 1)
        
#         textDecrypt += alphabet[indexAlphabet]

#     print(textDecrypt)

def ceasar(text, shift, code):
    textCeasar = ""
    for letter in text:
        if letter in alphabet:
            if "encode" in code:
                indexAlphabet = alphabet.index(letter) + shift
            else:
                indexAlphabet = alphabet.index(letter) - shift
            indexAlphabet %= (lenAlphabet+1)
            textCeasar += alphabet[indexAlphabet]
        else:
            textCeasar += letter
    print(f"Here's the {code}d result: {textCeasar}")

print(logo)

while userRetry is not False:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    if "encode" in direction:
        ceasar(text=text, shift=shift, code="encode")
    elif "decode" in direction:
        ceasar(text=text, shift=shift, code="decode")

    replyUser = input("try 'on' or 'no': ")
    if "on" in replyUser:
        userRetry = True
    else:
        userRetry = False
        print("Goodbye")