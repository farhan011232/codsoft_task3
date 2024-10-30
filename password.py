import random
import string 

length=int(input("enter lenght:"))

chars =string.ascii_letters
chars += string.digits
chars +=string.punctuation

password = " "

for i in range(length):
    new_character=random.choice(chars)
    password += new_character

print("Your random password is:",password)    