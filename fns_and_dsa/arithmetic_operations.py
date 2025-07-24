
def perform_operation(num1: float, num2: float, operation: str):
    '''
        description: fxn executes the arithmetic operation based on the operation parameter and the numerical values provided.
        parameters: num1 (float), num2 (float), operation (str) -> [add, subtract, multiply, divide]
        returns: result of the arithmetic operation (float) or an error message (str)
    '''
    
    operations = {
        'add': num1 + num2,
        'subtract': num1 - num2,
        'multiply': num1 * num2,
        'divide': num1 / num2 if num2 != 0 else "Error: Division by zero"
    }
    
    return operations.get(operation, "Error: Invalid operation")
