import random

name = input("What is your name? ")

print("Generating 5 passwords for " + name + "...")

for i in range(5):
    number = random.randint(100, 999)
    letter = random.choice(['A', 'B', 'C', 'D', 'E'])
    password = name + str(number) + letter + "!"
    print(password)
