import random

file = open("Random Numbers", "w+")
random.seed()
for i in range(30000):
    file.write(str(random.randint(-1000, 1000)) + ' ')
file.close()