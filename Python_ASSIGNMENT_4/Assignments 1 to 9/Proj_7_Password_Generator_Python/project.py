import random
import string

def generate_password(length=12):
    characters = string.digits + string.ascii_letters + string.punctuation + string.whitespace
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# User inputs

length = int(input("Enter the desired password length: "))

password = generate_password(length)
print("Your desired password that you generate is:", password)        