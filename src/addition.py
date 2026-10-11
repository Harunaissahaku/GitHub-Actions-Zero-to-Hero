

def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def main():
    print("Simple Calculator App")

    first = float(input("Enter first number: "))
    operator = input("Enter operator (+, -, *, /): ")
    second = float(input("Enter second number: "))

    if operator == "+":
        result = add(first, second)
    elif operator == "-":
        result = subtract(first, second)
    elif operator == "*":
        result = multiply(first, second)
    elif operator == "/":
        result = divide(first, second)
    else:
        print("Invalid operator")
        return

    print("Result:", result)


if __name__ == "__main__":
    main()
