import sys

# Get the list of numbers from user input
input_str = input("Enter a list of numbers separated by whitespace: ")

# Split the input string into a list of strings
numbers = input_str.split()

# Convert the list of strings to a list of numbers (ints or floats)
try:
    numbers = [int(num) for num in numbers]
except ValueError:
    try:
        numbers = [float(num) for num in numbers]
    except ValueError:
        print("Error: Invalid input. Please enter a list of numbers separated by whitespace.")
        sys.exit(1)

# Print out the list as a valid Python array
print(numbers)
