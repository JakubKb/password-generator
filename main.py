import random

password_length = int(input("How many characters would you like? "))
includes_chars = input("Do you want normal characters? (yes/no) ")
includes_special_chars = input("Do you want special characters? (yes/no) ")
includes_numbers = input("Do you want numbers? (yes/no) ")
basic_chars = 'qwertyuiopasdfghjklzxcvbnm'
numbers = '1234567890'
special_chars = '~!@#$%^&*()_+{}|:"<>?-=[]\;.,'
password = ""


for x in range(password_length):
    char_set = ""
    if includes_chars == "yes":
        char_set += basic_chars
    if includes_special_chars == "yes":
        char_set += special_chars
    if includes_numbers:
        char_set += numbers
    password += random.choice(char_set)

print(password)
