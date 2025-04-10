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