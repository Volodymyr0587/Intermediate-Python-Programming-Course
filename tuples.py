import sys
import timeit

mytuple = ("Leo", 32, "Boston")
mytuple2 = "Leo",
mytuple3 = tuple(["Leo", 32, "Boston"])
print(mytuple, mytuple2, mytuple3)

item = mytuple[0]
print(item)

letters = ('a', 'p', 'p', 'l', 'e')
print(len(letters))
print(letters.count('p'))
print(letters.index('p'))

letters_list = list(letters)
print(letters_list)

a = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

b = a[2:5]
print(b)

name, age, city = mytuple
print(name, age, city)

i1, *i2, i3 = a
print(i1, i2, i3)


some_list = [0, 1, 2, "Hello", True]
some_tuple = (0, 1, 2, "Hello", True)
print(sys.getsizeof(some_list), "bytes") # 104 bytes
print(sys.getsizeof(some_tuple), "bytes") # 80 bytes

print(timeit.timeit(stmt="[0, 1, 2, 3, 4, 5]", number=1000000))
print(timeit.timeit(stmt="(0, 1, 2, 3, 4, 5)", number=1000000))
