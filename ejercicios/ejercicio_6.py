amount_of_numbers = int(input("Please enter the number of numbers in the list: "))
numbers = 0
for i in range(0, amount_of_numbers):
    entered_number = float(input("Please enter one number: "))
    numbers += entered_number

print(f"The sum of the numbers in the list is: {numbers}.")
