import secrets
import string

def generate_password(length=12, use_uppercase=True, use_symbols=True) -> str:
    characters = string.ascii_lowercase + string.digits
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_symbols:
        characters += string.punctuation
    return ''.join(secrets.choice(characters) for _ in range(length))

if __name__ == "__main__":
    print(generate_password(length=25))
