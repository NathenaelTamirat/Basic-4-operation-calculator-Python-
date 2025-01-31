# Create a function that return the value based on operation 
def addition(a, b):
    return a + b
def subtraction(a, b):
    return a - b
def multiplication(a, b):
    return a * b
def division(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a / b

# This function provides a basic calculator for two numbers.    
def calculator():
# Print a welcome message for the user
    print("Welcome to the Basic 2 number adding Calculator!")
    print("Select operation:")
# User choice for the type of operation 
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

# Create while loop 
    while True:
            choice = input("Enter choice (1/2/3/4 or 'x' to quit): ")
            if choice.lower() == 'x':
                print("Exiting calculator. Thank you for using the calculator")
                break

            if choice not in ('1', '2', '3', '4'):
                print("Invalid input!. Please choose a valid operation.")
                continue

            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))

            if choice == '1':
                print(f"Result: {num1} + {num2} = {addition(num1, num2)}")
            elif choice == '2':
                print(f"Result: {num1} - {num2} = {subtraction(num1, num2)}")
            elif choice == '3':
                print(f"Result: {num1} * {num2} = {multiplication(num1, num2)}")
            elif choice == '4':
                print(f"Result: {num1} / {num2} = {division(num1, num2)}")

        except ValueError:
            print("Error!! Please enter valid numbers!")

if __name__ == "__main__":
    calculator()


