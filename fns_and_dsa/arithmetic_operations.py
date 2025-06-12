def perform_operation(num1: float, num2: float, operation: str):
    """
    Perform basic arithmetic operations and print the result.
    
    Parameters:
    num1 (float): First number
    num2 (float): Second number
    operation (str): Type of operation ('add', 'subtract', 'multiply', 'divide')
    """
    if operation == "add":
        print(num1 + num2)
    elif operation == "subtract":
        print(num1 - num2)
    elif operation == "multiply":
        print(num1 * num2)
    elif operation == "divide":
        print(num1 / num2 if num2 != 0 else "Error: Division by zero.")
    else:
        print("Error: Invalid operation.")

