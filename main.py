import random
import string
from datetime import datetime

PASSWORD_FILE = "popular_passwords.txt"
LOG_FILE = "password_log.txt"

def main():
    print("Password Manager")
    print("1 - Generate new password")
    print("2 - Check if password exists in database")
    print("3 - Exit")
    while True:
        choice = input("Your choice (1/2/3): ").strip()

        if choice == "1":
            try:
                length = int(input("Enter password length: "))
                if length <= 0:
                    print("Length must be greater than 0!")
                else:
                    password = generate_password(length)
                    print("Generated password:", password)
                    log_password(password)
            except ValueError:
                print("Invalid input! Please enter a number.")

        

        else:
            print("Invalid choice. Please enter 1, 2 or 3.")

if __name__ == "__main__":
    main()

def generate_password(length):
    """Generate a random password with given length"""
    chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(chars) for _ in range(length))
    return password

def log_password(password):
    """Log generated password with timestamp to log file"""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"{timestamp} - Generated password: {password}\n"

    try:
        with open(LOG_FILE, "a") as file:
            file.write(log_entry)
        print(f"Password logged to {LOG_FILE}")
    except IOError as e:
        print(f"Error writing to log file: {e}")