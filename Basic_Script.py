# Important elements:
# 1. Comments (start with #)
# These lines are for humans, not computers
# This is a really minor change

# 2. Imports
import math
import time
import numpy

# 3. Variables
radius = 7

# 4. Functions
def area_of_circle(r):
    return math.pi * (r ** 2)

# 5. Logic / Code Execution
area = area_of_circle(radius)
print(f"The area of a circle with radius {radius} is {area:.2f}")

# 6. Main guard (optional)
if __name__ == "__main__":
    print("Script executed directly!")
