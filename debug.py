# Example of debugging by identifying common mistakes
def greet():
    return "Hello"

# Wrong - forgot parentheses
message = greet  # This assigns the function object, doesn't call it
print(message)  # Prints function object, not "Hello"

# Right - with parentheses
message = greet()  # Actually calls the function
print(message)  # Prints "Hello"
# Examples of debugging by changing perspective
numbers = [1, 2, 3, 4]

# Intended to double each number but getting [1, 2, 3, 4]
for n in numbers:
    n = n * 2  # This doesn't modify the list
    
# Instead of asking why it's not doubling, ask why it's returning original list
# Answer: Because we're not storing the modified values back into the lis
# Example of debugging by eliminating possibilities
def calculate_total(items):
    total = 0
    for item in items:
        total += item['price'] * item['quantity']  # Bug isn't here
    return total * 1.08  # Sales tax - bug is here (should be 1.10)

# By testing calculate_total with known inputs, we can isolate 
# where the miscalculation occurs
#Example of debugging by explaining the problem

def find_max(nums):
    max_num = 0  # Bug for negative numbers
    for num in nums:
        if num > max_num:
            max_num = num
    return max_num

# Explaining out loud: "This function is supposed to find the maximum number,
# but if I pass [-1, -2, -3], it returns 0 which is wrong because..."
# This leads to realizing the initialization should be max_num = float('-inf')
# Example of debugging wrong documentation
# Returns the average of two numbers
def average(a, b):
    return a + b  # Comment says average but code does sum
    
# Don't trust the comment - the code is wrong
# Debugging by writing documentation
def process_data(data):
    # First we clean the data by removing None values
    cleaned = [x for x in data if x is not None]
    
    # Then we convert all strings to lowercase
    processed = [x.lower() if isinstance(x, str) else x for x in cleaned]
    
    # Finally we return the processed data
    return processed

# While writing this documentation, you might realize you forgot to handle 
# cases where x is not a string and has no .lower() method

