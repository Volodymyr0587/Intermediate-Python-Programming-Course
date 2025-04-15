import random
import secrets
import numpy as np


#//* RANDOM

""" 
a = random.random()
print(a)
a = random.uniform(1, 10)
print(a)
a = random.randint(1, 10)
print(a)
a = random.randrange(1, 10)
print(a)
a = random.normalvariate(0, 1)
print(a) 
"""


""" 
letters = list("ABCDEFGH")
print(random.choice(letters))
print(random.choices(letters, k=3)) #//% elements can be repeated
print(random.sample(letters, 3)) #//% elements are NOT repeating

random.shuffle(letters)
print(letters)
 """
 
""" 
random.seed(1)
print(random.random())
print(random.randint(1, 10))
random.seed(2)
print(random.random())
print(random.randint(1, 10))

random.seed(1)
print(random.random())
print(random.randint(1, 10))
random.seed(2)
print(random.random())
print(random.randint(1, 10))
 """
 
#======================================================
#//* SECRETS
""" 
a = secrets.randbelow(10)
print(a)

a = secrets.randbits(4)
print(a)


letters = list("ABCDEFGH")
a = secrets.choice(letters)
print(a)
 """

#//* NUMPY

a = np.random.rand(3)
# print(a)
 
a = np.random.rand(3, 3)
# print(a)

a = np.random.randint(0, 10)
# print(a)

a = np.random.randint(0, 10, 3)
# print(a)

a = np.random.randint(0, 10, (3, 4))
# print(a)

arr = np.array([[1,2,3], [4,5,6], [7,8,9]])
print(arr)
np.random.shuffle(arr)
print(arr)

np.random.seed(1)
print(np.random.rand(3, 3))
np.random.seed(1)
print(np.random.rand(3, 3))