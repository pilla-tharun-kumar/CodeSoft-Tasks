import secrets
import string

GROUPS = [string.ascii_lowercase, string.ascii_uppercase, string.digits, "!@#$%^&*()-_=+"]

def generate(length, complexity):
    if complexity not in range(1, 5): raise ValueError("Complexity must be 1-4")
    if length < complexity: raise ValueError("Length must cover every selected character group")
    groups = GROUPS[:complexity]
    chars = [secrets.choice(group) for group in groups]
    pool = "".join(groups)
    chars.extend(secrets.choice(pool) for _ in range(length - len(chars)))
    secrets.SystemRandom().shuffle(chars)
    return "".join(chars)

def main():
    try:
        length = int(input("Password length: "))
        complexity = int(input("Complexity (1 lowercase, 2 +uppercase, 3 +digits, 4 +symbols): "))
        print("Password:", generate(length, complexity))
    except ValueError as error: print("Error:", error)

if __name__ == "__main__": main()
