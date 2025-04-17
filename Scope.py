# Built-in scope example
# Python has a built-in `len` function
print("Built-in scope example: len([1, 2, 3]) =", len([1, 2, 3]))

# Global scope
x = "global"

def outer_function():
    # Enclosing scope
    x = "enclosing"

    def inner_function():
        # Local scope
        x = "local"
        print("Inside inner_function, x =", x)  # Local scope variable

    inner_function()
    print("Inside outer_function, x =", x)  # Enclosing scope variable

outer_function()
print("In global scope, x =", x)  # Global scope variable

# Demonstrating the `global` keyword
y = 10

def modify_global():
    global y  # Refers to the global variable `y`
    y = 20
    print("Inside modify_global, y =", y)

modify_global()
print("In global scope after modify_global, y =", y)

# Demonstrating the `nonlocal` keyword
def outer():
    z = "outer"

    def inner():
        nonlocal z  # Refers to the enclosing variable `z`
        z = "inner"
        print("Inside inner, z =", z)

    inner()
    print("Inside outer after inner, z =", z)

outer()