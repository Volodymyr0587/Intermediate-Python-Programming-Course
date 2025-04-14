""" x = -5
if x < 0:
    raise Exception("x should be positive")

assert (x >= 0), 'x is not positive' """


""" try:
    a = 5 / 0
    # b = 2 + '10'
    c = 10
except ZeroDivisionError as e:
    print(e)
except TypeError as e:
    print(e)
else:
    print("Everything is fine")    
finally:
    print("cleaning up...") """
    

class ValueTooHightError(Exception):
    pass

class ValueTooSmallError(Exception):
    def __init__(self, message, value):
        self.message = message
        self.value = value
    
    
    
def test_value(x):
    if x > 100:
        raise ValueTooHightError(f"value {x} is too hight")
    if x < 5:
        raise ValueTooSmallError("value is too small", x)

try:   
    # test_value(200)
    test_value(2)
except ValueTooHightError as e:
    print(e)
except ValueTooSmallError as e:
    print(e.message, e.value)