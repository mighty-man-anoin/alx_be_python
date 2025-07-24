
# def perform_operation(num1: float, num2: float, operation: str):
def perform_operation(num1, num2, operation):
    '''
        description: fxn executes the arithmetic operation based on the operation parameter and the numerical values provided.
        parameters: num1 (float), num2 (float), operation (str) -> [add, subtract, multiply, divide]
        returns: result of the arithmetic operation (float) or an error message (str)
    '''
    
    # better way to do this 
    
    # operations = {
    #     'add': num1 + num2,
    #     'subtract': num1 - num2,
    #     'multiply': num1 * num2,
    #     'divide': "Error: Division by zero" if num2 == 0 else num1 / num2,
    # }
    
    # return operations.get(operation, "Error: Invalid operation")
    
    # to pass checks for invalid operations
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            return "Error: Division by zero"
        return num1 / num2
    else:
        return "Error: Invalid operation"
