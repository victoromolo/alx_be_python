# multiplication_table.py

# Prompt the user for a number
number = int(input("Enter a number to see its multiplication table: "))

# Use for loop to generate and print the multiplication table
for i in range(1, 11):
    result = number * i
    print(f"{number} * {i} = {result}")

