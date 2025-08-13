# Write a python program to translate a message into secret code language. Use the rules below to translate normal English into secret code language

# Coding:
# if the word contains atleast 3 characters, remove the first letter and append it at the end now append three random characters at the starting and the end
# else:
#   simply reverse the string

# Decoding:
# if the word contains less than 3 characters, reverse it
# else:
#   remove 3 random characters from start and end. Now remove the last letter and append it to the beginning

# Your program should ask whether you want to code or decode

import random

def encode(word):
    if len(word) >= 3:
        encoded_word = word[1:] + word[0]
        encoded_word = ''.join([random.choice('abcdefghijklmnopqrstuvwxyz') for _ in range(3)]) + encoded_word + ''.join([random.choice('abcdefghijklmnopqrstuvwxyz') for _ in range(3)])
    else:
        encoded_word = word[::-1]
    return encoded_word

def decode(word):
    if len(word) < 3:
        decoded_word = word[::-1]
    else:
        word = word[3:-3]
        decoded_word = word[-1] + word[:-1]
    return decoded_word

def main():
    choice = input("Do you want to code or decode? (Enter 'code' or 'decode'): ").lower()
    if choice == 'code':
        word = input("Enter the word to encode: ")
        encoded_word = encode(word)
        print("Encoded word:", encoded_word)
    elif choice == 'decode':
        word = input("Enter the word to decode: ")
        decoded_word = decode(word)
        print("Decoded word:", decoded_word)
    else:
        print("Invalid choice. Please enter either 'code' or 'decode'.")

if __name__ == "__main__":
    main()