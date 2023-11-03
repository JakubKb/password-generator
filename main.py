import random
import os

while True:
    password_length = input("How many characters would you like? ")
    if not password_length.isdigit():
        print("Please enter a valid number for password length.")
    else:
        password_length = int(password_length)
        break

includes_chars = input("Do you want normal characters? (yes/no) ")
includes_special_chars = input("Do you want special characters? (yes/no) ")
includes_numbers = input("Do you want numbers? (yes/no) ")
basic_chars = 'qwertyuiopasdfghjklzxcvbnm'
numbers = '1234567890'
special_chars = '~!@#$%^&*()_+{}|:"<>?-=[]\;.,'
copy_password = input("Do you want your password copied to clipboard? (yes/no) ")
password = ""

for x in range(password_length):
    char_set = ""
    if includes_chars == "yes":
        char_set += basic_chars
    if includes_special_chars == "yes":
        char_set += special_chars
    if includes_numbers == "yes":
        char_set += numbers
    password += random.choice(char_set)

print(password)

if copy_password == "yes":
    def add_to_clipoard(text):
        command = 'echo ' + text + '| xclip -selection clipboard'
        os.system(command)

    add_to_clipoard(password)
    print("Password has been copied to the clipboard.")
