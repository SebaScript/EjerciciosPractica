import random

quantity = int(input("How many numbers do you want to generate?: "))
for i in range(quantity):
    print(random.randint(0, 1000000))
