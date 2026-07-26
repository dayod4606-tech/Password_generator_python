import secrets
import string

def generate_password():
    print("--- PASSWORD GENERATOR ---")

    while True:
        length_input = input("Enter password length (12): ")
        try:
            length = int(length_input)
            if length < 4:
                print("Please choose a length of at least 4.")
                continue
            break
        except ValueError:
            print("That's not a number. Try again.")

    characters = string.ascii_letters + string.digits
    password = ''.join(secrets.choice(characters) for _ in range(length))

    print(f"\nYour generated password: {password}")

if __name__ == "__main__":
    generate_password()