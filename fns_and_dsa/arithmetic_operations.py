def perform_operation(num1: float, num2: float, operation: str):
    """
    Performs basic arithmetic operations on two numbers.

    Args:
        num1 (float): The first number.
        num2 (float): The second number.
        operation (str): The arithmetic operation to perform.
                         Accepted values are 'add', 'subtract', 'multiply', 'divide'.

    Returns:
        float or str: The result of the operation, or an error message if division by zero occurs
                      or an invalid operation is provided.
    """
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        # Handle division by zero
        if num2 == 0:
            return "Error: Division by zero is not allowed."
        return num1 / num2
    else:
        # Handle invalid operation input
        return "Error: Invalid operation. Please choose from 'add', 'subtract', 'multiply', or 'divide'."
