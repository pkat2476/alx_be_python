
def perform_operation(num1: float, num2: float, operation: str):
    """
    Performs a basic arithmetic operation between two numbers.

    Args:
        num1 (float): The first number.
        num2 (float): The second number.
        operation (str): The operation to perform ('add', 'subtract', 'multiply', 'divide').

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
        if num2 == 0:
            return "Error: Cannot divide by zero."
        else:
            return num1 / num2
    else:
        return "Error: Invalid operation specified. Please choose 'add', 'subtract', 'multiply', or 'divide'."

