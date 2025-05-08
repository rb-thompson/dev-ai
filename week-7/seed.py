import random
random.seed(5)
print(random.random())

from datetime import datetime

date1 = datetime(2023, 10, 1)
date2 = datetime(2023, 10, 15)
difference = date2 - date1
print(difference.days)