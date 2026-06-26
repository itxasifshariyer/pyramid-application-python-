
def calculate():
    print("=== Classic Python Calculator ===")
    
    # 1. Take inputs from the user
    # We convert the inputs to float so the calculator can handle decimals
    try:
        num1 = float(input("Enter the first number: "))
        operator = input("Enter an operator (+, -, *, /): ").strip()
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Error: Invalid input. Please enter numbers only.")
        return

    # 2. Perform the calculation based on the operator using if-elif-else logic
    if operator == '+':
        result = num1 + num2
        print(f"Result: {num1} + {num2} = {result}")
        
    elif operator == '-':
        result = num1 - num2
        print(f"Result: {num1} - {num2} = {result}")
        
    elif operator == '*':
        result = num1 * num2
        print(f"Result: {num1} * {num2} = {result}")
        
    elif operator == '/':
        # Critical Check: Prevent division by zero
        if num2 == 0:
            print("Error: Division by zero is not allowed.")
        else:
            result = num1 / num2
            print(f"Result: {num1} / {num2} = {result}")
            
    else:
        print("Error: Invalid operator. Please use +, -, *, or /.")

# Run the calculator function
calculate()