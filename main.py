```python
import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

def exponent(x, y):
    return x ** y

def modulus(x, y):
    return x % y

def square_root(x):
    return math.sqrt(x)

def display_menu():
    print("\nSimple Advanced Calculator")
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exponentiation (x^y)")
    print("6. Modulus (x % y)")
    print("7. Square Root (√x)")
    print("8. View History")
    print("9. Clear Memory")
    print("0. Exit")

def calculator():
    history = []
    memory = None

    while True:
        display_menu()
        choice = input("Enter choice (0-9): ")

        if choice == '0':
            print("Exiting the calculator. Goodbye!")
            break

        elif choice == '8':
            print("Calculation History:")
            for record in history:
                print(record)
            continue

        elif choice == '9':
            memory = None
            print("Memory cleared.")
            continue

        elif choice in ['1', '2', '3', '4', '5', '6']:
            if memory is not None:
                use_memory = input("Use stored result in memory? (y/n): ").lower()
                if use_memory == 'y':
                    num1 = memory
                    print(f"First number: {num1}")
                else:
                    num1 = float(input("Enter first number: "))
            else:
                num1 = float(input("Enter first number: "))

            num2 = float(input("Enter second number: "))

            if choice == '1':
                result = add(num1, num2)
                operation = '+'

            elif choice == '2':
                result = subtract(num1, num2)
                operation = '-'

            elif choice == '3':
                result = multiply(num1, num2)
                operation = '*'

            elif choice == '4':
                result = divide(num1, num2)
                operation = '/'

            elif choice == '5':
                result = exponent(num1, num2)
                operation = '^'

            elif choice == '6':
                result = modulus(num1, num2)
                operation = '%'

            history.append(f"{num1} {operation} {num2} = {result}")
            print(f"Result: {result}")
            memory = result

        elif choice == '7':
            num = float(input("Enter number: "))
            result = square_root(num)
            print(f"Square root of {num} is {result}")
            history.append(f"√{num} = {result}")
            memory = result

        else:
            print("Invalid input! Please choose a valid option.")

if __name__ == "__main__":
    calculator()
