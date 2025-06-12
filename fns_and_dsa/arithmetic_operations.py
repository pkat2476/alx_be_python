def perform_operation(num1: float, num2: float, operation: str):
    """
    Perform basic arithmetic operations.
    
    Parameters:
    num1 (float): First number
    num2 (float): Second number
    operation (str): Type of operation ('add', 'subtract', 'multiply', 'divide')
    
    Returns:
    float or str: The result of the operation, or an error message for division by zero.
    """
    if operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        return num1 / num2 if num2 != 0 else "Error: Division by zero."
    else:
        return "Error: Invalid operation."

