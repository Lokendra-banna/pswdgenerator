import random
import string

def generate_password(length):
    # Define the character set to choose from
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate the password randomly
    password = ''.join(random.choice(characters) for i in range(length))6
    return password

# Prompt the user to enter the desired length of the password
try:
    desired_length = int(input("Enter the desired length of the password: "))
    if desired_length <= 0:
        raise ValueError("Length must be a positive integer")
    
    # Generate the password
    generated_password = generate_password(desired_length)
    
    # Display the generated password
    print(f"Generated password of length {desired_length}: {generated_password}")

except ValueError as ve:
    print(f"Error: {ve}")
