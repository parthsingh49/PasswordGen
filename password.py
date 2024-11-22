import random
import string

def generate_password(pass_length=12):
    # Ensure the password length is reasonable
    if pass_length < 4:
        return "Password length should be at least 4 characters!"

    # Define character sets for password generation
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    numbers = string.digits
    symbols = string.punctuation

    # Guarantee inclusion of at least one character from each set
    mandatory_chars = [
        random.choice(lowercase_letters),
        random.choice(uppercase_letters),
        random.choice(numbers),
        random.choice(symbols),
    ]

    # Combine all character sets
    all_characters = lowercase_letters + uppercase_letters + numbers + symbols

    # Fill the remaining length with random characters
    remaining_chars = random.choices(all_characters, k=pass_length - 4)

    # Combine mandatory and random characters
    password_chars = mandatory_chars + remaining_chars

    # Shuffle to ensure randomness
    random.shuffle(password_chars)

    # Return the password as a string
    return ''.join(password_chars)

# Input desired password length and generate the password
try:
    length = int(input("Enter the desired length of the password: "))
    generated_password = generate_password(length)
    print("Your Secure Password: ", generated_password)
except ValueError:
    print("Please enter a valid number!")