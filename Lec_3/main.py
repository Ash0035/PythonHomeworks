
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

def get_operation(choice):
    operations = {
        '+': add,
        '-': subtract,
        '*': multiply,
        '/': divide
    }
    return operations.get(choice)

def main():
    print("Welcome to the Simple Calculator!")
    
    while True:
        print("\nSelect operation:")
        print("+. Add")
        print("-. Subtract")
        print("*. Multiply")
        print("/. Divide")
        print("x. Exit")
        
        
        choice = input("Enter choice (+,-,*,/,x): ")
        
        if choice == 'x':
            print("Exiting the calculator. Goodbye!")
            break
        
        if choice in ['+', '-', '*', '/']:
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
                
                operation = get_operation(choice)
                result = operation(num1, num2)
                print(f"Result: {result}")
            
            except ValueError:
                print("Invalid input! Please enter numeric values.")
        else:
            print("Invalid choice! Please select a valid operation.")

if __name__ == "__main__":
    main()
