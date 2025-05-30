import random
import string #this allows you to import like collections of this like (punctuation, words, and so on)

chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
key = chars.copy()

random.shuffle(key)

#print(f"chars: {chars}")
#print(f"key: {key}")
#Encrypt

while True:
    print("----Menu-----")
    print("1. Encrypt(e)")
    print("2. Decrypt(d)")
    print("3. Leave(l)")
    print("-------------\n")
    choice = input("chose and option:")
    if choice.lower() == "e":
        plain_text = input("Enter a message to encrypt: ")
        cipher_text = ""

        for letter in plain_text:
            index = chars.index(letter)
            cipher_text += key[index]

        print(f"original message: {plain_text}")
        print(f"cipher text: {cipher_text}")

    elif choice.lower() == "d":
        print()
        cipher_text = input("Enter a message to decrypt: ")
        plain_text = ""


        for letter in cipher_text:
            index = key.index(letter)
            plain_text += chars[index]

        print(f"cipher text: {cipher_text}")
        print(f"Decrypted text: {plain_text}")
    elif choice.lower() == "l":
            break