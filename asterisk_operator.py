
#//% * * * * * * * * * *

result = 2 * 4
print(result) # 8
result = 2 ** 4
print(result) # 16


zeros = [0] * 10
print(zeros) # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

def foo(a, b, *args, **kwargs):
    print(a, b)
    for arg in args:
        print(arg)
    for key in kwargs:
        print(key, kwargs[key])
        
        
foo(1, 2, 3, 4, 5, six=6, seven=7)


#//% keyword only parameters after *
def foo(a, b, *, c):
    print(a, b, c)
    
foo(1, 2, c=3)

#//% unpack collections
def foo(a, b, c):
    print(a, b, c)
    
my_list = [0, 1, 2]
foo(*my_list)
    
my_dict = {'a': 1, 'b': 2, 'c': 3}
foo(**my_dict)

numbers = [1, 2, 3, 4, 5, 6]

*beginning, last = numbers
print(beginning) # [1, 2, 3, 4, 5]
print(last) # 6

beginning, *middle, second_last, last = numbers
print(beginning) # 1
print(middle) # [2, 3, 4]
print(second_last) # 5
print(last) # 6

#//% merge iterable
my_tuple = (1, 2, 3)
my_list = [4, 5, 6]
my_set = {7, 8, 9}

merged_iters = [*my_tuple, *my_list, *my_set]
print(merged_iters) # [1, 2, 3, 4, 5, 6,  8, 9, 7]

dict_a = {'a': 1, 'b': 2}
dict_b = {'c': 2, 'd': 4}
merged_dicts = {**dict_a, **dict_b}
print(merged_dicts) # {'a': 1, 'b': 2, 'c': 2, 'd': 4}