# A simple script with a logic bug to demonstrate VS Code debugging
# Add breakpoints on lines 6, 7, 8 to see the functionality of the debugger.
my_global_variable = "This is what a global variable looks like"

def calculate_average(numbers):
    total = 0
    for n in numbers:
        total = total + n # Set a break point here
    average = total / len(numbers)  # Watch this in the debugger
    return average

def main():
    # numbers = [2, 4, 6, 8, 10]
    # print("Numbers:", numbers)
    # result = calculate_average(numbers)
    # print("The average is:", result)  # Expect 6.0

    # Uncomment this after you have experienced issue-free debugger execution

    # Introduce a bug:
    wrong_result = calculate_average([2, 4, 6, 8, 10])  # ⚠️ This will cause an error
    print("The average (buggy) is:", wrong_result)

if __name__ == "__main__":
    main()
