import random
import string

def generate_password(length, use_digits=True, use_letters=True, use_special_chars=True):
    characters = ''
    if use_digits:
        characters += string.digits
    if use_letters:
        characters += string.ascii_letters
    if use_special_chars:
        characters += string.punctuation

    if not characters:
        return "Please select at least one character type."

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    while True:
        length = int(input("Enter the desired password length: "))
        use_digits = input("Include digits? (yes/no): ").lower() == 'yes'
        use_letters = input("Include letters? (yes/no): ").lower() == 'yes'
        use_special_chars = input("Include special characters? (yes/no): ").lower() == 'yes'

        password = generate_password(length, use_digits, use_letters, use_special_chars)
        print("Generated Password:", password)

        satisfaction = input("Are you satisfied with the password? (yes/no): ").lower()
        if satisfaction == 'yes':
            break

if __name__ == "__main__":
    main()
