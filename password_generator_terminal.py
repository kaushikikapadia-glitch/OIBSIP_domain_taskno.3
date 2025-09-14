import random
import string
import pyperclip  # optional, for clipboard copy

# Function to generate password
def generate_password(length, use_upper=True, use_numbers=True, use_symbols=True):
    characters = string.ascii_lowercase
    if use_upper:
        characters += string.ascii_uppercase
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Main program
def main():
    print("=== Advanced Terminal Random Password Generator ===\n")
    while True:
        try:
            length = int(input("Enter password length (8-50): "))
            if length < 8 or length > 50:
                print("Password length must be between 8 and 50. Try again.")
                continue
        except ValueError:
            print("Invalid input. Enter numeric values only.")
            continue

        use_upper = input("Include uppercase letters? (yes/no): ").strip().lower() == 'yes'
        use_numbers = input("Include numbers? (yes/no): ").strip().lower() == 'yes'
        use_symbols = input("Include symbols? (yes/no): ").strip().lower() == 'yes'

        password = generate_password(length, use_upper, use_numbers, use_symbols)
        print(f"\nGenerated Password: {password}")

        # Copy to clipboard
        try:
            pyperclip.copy(password)
            print("Password copied to clipboard!")
        except:
            print("Clipboard copy failed (pyperclip not installed).")

        cont = input("\nDo you want to generate another password? (yes/no): ").strip().lower()
        if cont != 'yes':
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()
