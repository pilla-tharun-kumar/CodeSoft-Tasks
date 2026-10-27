def calculate(a, b, operation):
    if operation == "+": return a + b
    if operation == "-": return a - b
    if operation == "*": return a * b
    if operation == "/":
        if b == 0: raise ValueError("Cannot divide by zero")
        return a / b
    raise ValueError("Choose +, -, * or /")

def main():
    try:
        a = float(input("First number: "))
        b = float(input("Second number: "))
        operation = input("Operation (+, -, *, /): ").strip()
        print("Result:", calculate(a, b, operation))
    except ValueError as error: print("Error:", error)

if __name__ == "__main__": main()
