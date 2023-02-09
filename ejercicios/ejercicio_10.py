number = int(input("Please enter the number: "))
fact = 1

for i in range(1, number + 1):
    fact *= i
print(f"The result of {number}! is: {fact}.")
