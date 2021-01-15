import random
import datetime
print(datetime.datetime.now())
numbers = range(1,46)

lucky_numbers = random.sample(numbers,6)
print(sorted(lucky_numbers))