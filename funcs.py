def print_name(name):  # name - parameter
    print(name)
    
# print_name("Alex")      # "Alex" - argument

def foo(a, b ,c, d=4):
    print(a, b, c, d)
    
# foo(1, b=2, c=3)

def foo(a, b, *args, **kwargs):
    print(a, b)
    for arg in args:
        print(arg)
    for key in kwargs:
        print(key, kwargs[key])
               
# foo(1, 2, 3, 4, 5, six=6, seven=7)


def foo(a, b, *, c, d):
    print(a, b, c ,d)
  
  
# foo(1, 2, c=3, d=4)      

def foo(a, b, c):
    print(a, b, c)
    
my_list = [0, 1, 2]
# foo(*my_list)
my_dict = {'a': 1, 'b': 2, 'c': 3}
# foo(**my_dict)



def foo():
    global number
    number = 3

number = 0
foo()
# print(number)



def foo(a_list):
    a_list.append(4)
    a_list[0] = -100

my_list = [1, 2, 3]
foo(my_list)
print(my_list) # [-100, 2, 3, 4]