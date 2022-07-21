from multiprocessing import pool
import random
print("\nCreate a list of random integers")
population = range(0,100)
num_list = random.sample(population,10)
print(num_list)
no_elements = 4
print("\nRandomly select",no_elements,"multiple items from the said list")
result_elements = random.sample(num_list,no_elements)
print(result_elements)
no_elements = 8
print("Randomly select",no_elements,"multiple items from the said list")
result_elements = random.sample(num_list,no_elements)
print(result_elements)