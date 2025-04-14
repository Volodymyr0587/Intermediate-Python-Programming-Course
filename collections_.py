# Counter, namedtuple, OrderDict, defaultdict, deque
from collections import Counter
from collections import namedtuple
from collections import OrderedDict
from collections import defaultdict
from collections import deque


#//% COUNTER

a = "aaaaabbbbbbbbbccccccccc"
my_counter = Counter(a)
print(my_counter)
# print(my_counter.keys())
# print(my_counter.values())
print(my_counter.most_common())
print(my_counter.most_common(1))
print(my_counter.most_common(1)[0][0])
print(list(my_counter.elements()))


#//% NAMED TUPLE
Point = namedtuple('Point', 'x,y')
pt = Point(1, -4)
print(pt)
print(pt.x, pt.y)


#//% ORDERED DICT (since python 3.7 regular dict also ordered)
ordered_dict = OrderedDict()
ordered_dict['a'] = 1
ordered_dict['b'] = 2
ordered_dict['c'] = 3
ordered_dict['d'] = 4
print(ordered_dict)


#//% DEFAULTDICT
d = defaultdict(int) # float, list ...
d['a'] = 1
d['b'] = 2

print(d)
print(d['a'])
print(d['c']) # 0

#//% DEQUE
dq = deque()
print(dq)  # deque([])

dq.append(1)
print(dq) # deque([1])

dq.append(2)
print(dq) # deque([1, 2])

dq.appendleft(3)
print(dq) # deque([3, 1, 2])

dq.pop() # 2
print(dq) # deque([3, 1])

dq.popleft() # 3
print(dq) # deque([1])

dq.clear()
print(dq) # deque([])

dq.extend([4, 5, 6])
print(dq) # deque([4, 5, 6])

dq.extendleft([1, 2, 3])
print(dq) # deque([3, 2, 1, 4, 5, 6])

dq.rotate()
print(dq) # deque([6, 3, 2, 1, 4, 5])

dq.rotate(2)
print(dq) # deque([4, 5, 6, 3, 2, 1])

dq.rotate(-1)
print(dq) # deque([5, 6, 3, 2, 1, 4])