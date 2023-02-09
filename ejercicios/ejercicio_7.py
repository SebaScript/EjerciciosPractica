list_numbers = []
entered_number = 0
decision = 1
i = 1
sum = 0
while decision == 1:
    entered_number = float(input(f"Please enter the number{str(i)}:"))
    list_numbers.append(entered_number)
    i = i + 1
    decision = int(input("Do you want to add other number?: (1: yes ; 0: no)"))

largest_number = max(list_numbers)
smallest_number = min(list_numbers)

print(f"The numbers in the list are: {list_numbers}.")
print(f"The largest number is: {largest_number}.")
print(f"The smallest number is: {smallest_number}.")
