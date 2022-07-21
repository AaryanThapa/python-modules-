import random
import datetime
print("\nGenreate random integer between 0 and 6:")
print(random.randrange(5))
print("Generate random integer between 5 and 10, excluding 10")
print(random.randrange(start=5, stop=10))
print("Genrate random integer between 0 ande 20, with a step of 3")
print(random.randrange(start=0, step=3, stop=10))
print("\nRandom date between two dates")
start_dt = datetime.date(2022,4,1)
end_dt = datetime.date(2022,5,1)
time_between_dates = end_dt - start_dt
days_between_dates = time_between_dates.days
random_number_of_days = random.randrange(days_between_dates)
random_days = start_dt + datetime.timedelta(days = random_number_of_days)
print(random_days)
