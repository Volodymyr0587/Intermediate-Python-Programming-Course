import sys

""" def mygenerator():
    yield 1
    yield 2
    yield 3
    
g = mygenerator() """

""" for i in g:
    print(i) """
    
""" value = next(g)
print(value)
value = next(g)
print(value)
value = next(g)
print(value)
value = next(g)
print(value) """

# print(sum(g))

""" def countdown(num: int):
    print("Starting")
    while num > 0:
        yield num
        num -= 1
        
cd = countdown(4)

value = next(cd)
print(value)

print(next(cd)) """


""" def firstn_generator(n):
    num = 0
    while num < n:
        yield num
        num += 1
        
print(sum(firstn_generator(10))) """


""" def fibonacci(limit):
    # 0 1 1 2 3 5 8 13 ...
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a + b
        
fib = fibonacci(30)
for i in fib:
    print(i) """
    
    
even_generator = (i for i in range(100000) if i % 2 == 0)
print(next(even_generator)) # 0
print(next(even_generator)) # 2
print(next(even_generator)) # 4

even_list = [i for i in range(100000) if i % 2 == 0]

print(sys.getsizeof(even_generator)) # 104
print(sys.getsizeof(even_list)) # 444376
