from random import *

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


print("Welcome to the PyPassword Generator!")

letter = int(input("How many letters would you like in your password?\n"))
number = int(input("How many numbers would you like?\n"))
symbol = int(input("How many symbols would you like?\n"))


password = ""

for i in range(letter):
    r_letter = (choice(letters))
    password += r_letter

for j in range(number):
    r_number = (choice(numbers))
    password += r_number

for k in range(symbol):
    r_symbol = (choice(symbols))
    password += r_symbol


password_list = list(password)
shuffle(password_list)

pyPassword = ""
for l in password_list:
    pyPassword += l

print(pyPassword)


