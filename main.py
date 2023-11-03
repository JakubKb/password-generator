import random

password_lenght = int(input("How many characters would you like? "))
includes_chars = input("do you want normal characters?(yes/no)")
includes_special_chars = input("do you want special characters?(yes/no)")
includes_numbers = input("do you want numbers?(yes/no)")
basic_chars = 'qwertyuiopasdfghjklzxcvbnm'
numbers = '1234567890'
special_chars = '~!@#$%^&*()_+{}|:"<>?-=[]\;.,'
password = ""

for x in range(password_lenght):
    if includes_chars == "yes" and includes_numbers == "no" and includes_special_chars == "no":
        password += random.choice(basic_chars)

print(password)
