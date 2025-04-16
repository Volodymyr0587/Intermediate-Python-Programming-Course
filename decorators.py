import functools

#//% Function decorator
""" 
@mydecorator
def dosomething():
    pass
"""

def my_decorator(func):
    
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Do something before...
        result = func(*args, **kwargs)
        # Do something after...
        return result
    return wrapper

def start_end_decorator(func):
    
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("Start")
        result = func(*args, **kwargs)
        print("End")
        return result
    return wrapper


        

""" 
@start_end_decorator
def print_name():
    print("Alex")
    
    
# print_name = start_end_decorator(print_name)

print_name() 
"""

@start_end_decorator
def add5(num: int) -> int:
    return num + 5

# print(add5(10))
# result = add5(10)
# print(result)

# print(help(add5))
# print(add5.__name__)


# ================================================

""" def repeat(num_times):
    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator_repeat

@repeat(num_times=3)
def greet(name):
    print(f"Hello {name}") 
    
greet("Alex") """

# ================================================


def debug(func):
    """a decorator function that prints debug information about the wrapped function"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
        signature = ", ".join(args_repr + kwargs_repr)
        print(f"Calling {func.__name__}({signature})")
        result = func(*args, **kwargs)
        print(f"{func.__name__!r} returned {result!r}")
        return result
    return wrapper


@debug
@start_end_decorator
def say_hello(name):
    greeting = f"Hello {name}"
    print(greeting)
    return greeting

# say_hello("Alex")

#//% =============== CLASS  DECORATOR =================================

class CountCalls:
    
    def __init__(self, func):
        self.func = func
        self.num_calls = 0
        
    def __call__(self, *args, **kwargs):
        self.num_calls += 1
        print(f"This is executed {self.num_calls} times")
        return self.func(*args, **kwargs)

@CountCalls
def say_hello():
    print("hello")
    
say_hello()
say_hello()
