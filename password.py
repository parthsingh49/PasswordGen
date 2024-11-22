import random
import string

def pass_gen(length = 12):
    if length < 4:
        return "Please input more than 4 characters!!!"
    
    
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    special = string.punctuation

    password = [random.choice(lower), random.choice(upper), random.choice(digits), random.choice(special)]

    all_char = lower + upper + digits + special
    password += random.choices(all_char, k=length-4)

    random.shuffle(password)

    return ''.join(password)

password_length = int(input("Enter the desired length of the password: "))
password = pass_gen(password_length)
print("Generated Password: ", password)