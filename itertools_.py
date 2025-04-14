# //% itertools: product, permutations, combinations, accumulate, groupby, and infinite iterators
from itertools import product
from itertools import permutations
from itertools import combinations
from itertools import combinations_with_replacement
from itertools import accumulate
from itertools import groupby
from itertools import count, cycle, repeat
import operator


# //% PRODUCT
a = [1, 2]
b = [3, 4]
prod = product(a, b)
print(list(prod))  # [(1, 3), (1, 4), (2, 3), (2, 4)]
prod = product(a, b, repeat=2)
print(
    list(prod)
)  # [(1, 3, 1, 3), (1, 3, 1, 4), (1, 3, 2, 3), (1, 3, 2, 4), (1, 4, 1, 3), (1, 4, 1, 4), (1, 4, 2, 3), (1, 4, 2, 4), (2, 3, 1, 3), (2, 3, 1, 4), (2, 3, 2, 3), (2, 3, 2, 4), (2, 4, 1, 3), (2, 4, 1, 4), (2, 4, 2, 3), (2, 4, 2, 4)]
print("=" * 40)

# //% PERMUTATION
a = [1, 2, 3]
print(
    list(permutations(a))
)  # [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]
print(list(permutations(a, r=2)))  # [(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]
print("=" * 40)

# //% COMBINATION
a = [1, 2, 3, 4]
print(list(combinations(a, 2)))  # [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]
print(
    list(combinations_with_replacement(a, 2))
)  # [(1, 1), (1, 2), (1, 3), (1, 4), (2, 2), (2, 3), (2, 4), (3, 3), (3, 4), (4, 4)]
print("=" * 40)

# //% ACCUMULATE
a = [1, 2, 3, 4]
print(list(accumulate(a)))  # [1, 3, 6, 10]
print(list(accumulate(a, func=operator.mul)))  # [1, 2, 6, 24]
a = [1, 2, 5, 3, 4]
print(list(accumulate(a, func=max)))  # [1, 2, 5, 5, 5]
print("=" * 40)

# //% GROUPBY
a = [1, 2, 3, 4]
group_obj = groupby(a, key=lambda x: x < 3)
print(group_obj)  # <itertools.groupby object at 0x744d9fca5620>
for key, value in group_obj:
    print(key, list(value))  # True [1, 2] False [3, 4]

print("." * 40)
# ==========
persons = [
    {"name": "Tim", "age": 25},
    {"name": "Dan", "age": 25},
    {"name": "Lisa", "age": 27},
    {"name": "Claire", "age": 28},
]
group_obj = groupby(persons, key=lambda person: person['age'])
for key, value in group_obj:
    print(key, list(value))
""" 25 [{'name': 'Tim', 'age': 25}, {'name': 'Dan', 'age': 25}]
27 [{'name': 'Lisa', 'age': 27}]
28 [{'name': 'Claire', 'age': 28}] """
print("=" * 40)

# //% COUNT, CYCLE, REPEAT
for i in count(10):
    print(i)
    if i == 15:
        break
    
    
a = [1, 2, 3]
stop = 10
for i in cycle(a):
    print(i)
    stop -= 1
    if stop == 0:
        break
    
    
for i in repeat(1, 10):
    print(i)