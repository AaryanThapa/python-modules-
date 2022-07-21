import random
import string
print("Generate a random color hex")
print("#{:07x}".format(random.randint(0,0xFFFFFF)))
print("\nGenrate a random alphabetical string:")
max_length = 255
s = ""
for i in range(random.randint(1,max_length)):
    s += random.choice(string.ascii_letters)
print(s)
print("Generate a random value between two integers, inculsive")
print(random.randint(0,10))
print(random.randint(-9,9))
print(random.randint(12,50))
print("Generate a random multiple of 7 between 0 and 70")
print(random.randint(0,10)*7)
