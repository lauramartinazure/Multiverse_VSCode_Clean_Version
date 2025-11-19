# ==============================================
# Debugger Navigation Demonstration
# Shows the difference between Step Over, Step Into, Step Out
# 1. Create breakpoint on line 39, 43, 47
#    Step over: you'll skip the internals of 'greet user'
# 2. Step Into: When you reach result = calculate_area(5), press F11 (Step Into).
#    You’ll jump inside calculate_area(), and then to the line calling square(radius).
# 3. Step Out: After entering square(), press Shift + F11.
#    VS Code finishes the rest of square() automatically, returning you to calculate_area().
# ==============================================
# This is a second minor change

def greet_user(name):
    """A simple function that prints a greeting."""
    print(f"Hello, {name}! Good afternoon")  # Step into here to see inside greet_user

def multiply(a, b):
    """Returns a * b and prints a message."""
    print(f"Multiplying {a} * {b}")
    result = a * b
    return result

def calculate_area(radius):
    """Calculates the area of a circle using a helper function."""
    pi = 3.14159
    squared = square(radius)     # <-- Great place to Step Into
    area = pi * squared
    print(f"Area for radius {radius}: {area:.2f}")
    return area

def square(x):
    """Helper function to demonstrate Step Into and Step Out."""
    print(f"Squaring {x}")
    return x * x

def main():
    print("=== Debug Navigation Demo ===")
    
    # Step Over: executes greet_user as a single action
    greet_user("Laura")

    # Step Into: go inside calculate_area to watch it call square()
    result = calculate_area(5)
    print(f"Result from calculate_area: {result:.2f}")

    # Step Over again: runs multiply without diving inside
    product = multiply(3, 4)
    print(f"Product: {product}")

    print("=== End of Program ===")

if __name__ == "__main__":
    main()
