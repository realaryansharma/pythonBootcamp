import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
symbols = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

password = ''

charSize = int(input("How many Characters do you want to add : "))
numSize = int(input("How many Numbers do you want to add : "))
specSize = int(input("How many Symbols do you want to add : "))

for i in range(0, charSize):
    password += random.choice(letters)

for i in range(0, numSize):
    password += random.choice(numbers)

for i in range(0, specSize):
    password += random.choice(symbols)

l = list(password)
random.shuffle(l)
result = ''.join(l)

print("\n\nYour password is : " + result)