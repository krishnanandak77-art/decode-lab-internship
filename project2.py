import string
import secrets

def generate_password():
    print("--- Flexible Password Generator ---")
    
    while True:
        try:
            length = int(input("How long do you want your password to be? "))
            if length <= 0:
                print("Length must be greater than 0!")
                continue
            elif length < 12:
                print("⚠️ Note: Passwords shorter than 12 characters are easier to crack.")
            break
        except ValueError:
            print("Please enter a valid whole number.")

    # Character pool: A-Z, a-z, 0-9
    character_pool = string.ascii_letters + string.digits
    password = ''.join(secrets.choice(character_pool) for _ in range(length))

    print("\n--------------------------------")
    print(f"Your {length}-character password is: {password}")
    print("--------------------------------")

if __name__ == "__main__":
    generate_password()
