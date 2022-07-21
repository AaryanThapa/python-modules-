import random
import os
print("Select random elements from list")
elments = (1,4,5,8,9,6,7)
print(random.choice(elments))
print(random.choice(elments))
print(random.choice(elments))
print("\nSelect random elements from set")
elments = ([1,4,5,6,7,8,2])
#convert set into tuple because sets are invalid input
print(random.choice(tuple(elments)))
print(random.choice(tuple(elments)))
print(random.choice(tuple(elments)))
print("\nSelect random elements from dictionary")
elments = {"a":2,"b":3,"c":4,"d":5,"e":7}
key = random.choice(list(elments))
print(elments[key])
key = random.choice(list(elments))
print(elments[key])
key = random.choice(list(elments))
print(elments[key])
print("Random file from directory")
print(random.choice(os.listdir("/")))