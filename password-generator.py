import string
import random

character_pool = "".join([string.ascii_letters, string.digits, string.punctuation])


def generate_password(password_length):
    password = []

    for i in range(password_length):
        random_char = random.choice(character_pool)
        password.append(random_char)
    return "".join(password)


length = input("What should the password length be?(Default 10): ")

if length.isnumeric():
    length = int(length)
else:
    length = 10

print(generate_password(length))

