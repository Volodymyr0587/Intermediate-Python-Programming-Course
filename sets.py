myset = {1, 2, 3, 1 ,2}
print(myset)

newset = set([1, 2, 3])
print(newset)

fromstring = set("hello")
print(fromstring)

another_set = set()
another_set.add(1)
another_set.add(2)
another_set.add(3)

print(another_set)
another_set.remove(2) #//% if element not in set - rise error
print(another_set)

another_set.discard(6) #//% if element not in set - NOT errors
print(another_set)

another_set.clear()
print(another_set)

print(newset.pop())
print(newset)

#//% union, intersection, difference
odds = {1, 3, 5, 7, 9}
evens = {0, 2, 4, 6, 8}
primes = {2, 3, 5, 7}

setA = {1, 2, 3, 4, 5, 6}
setB = {1, 2, 3}
setC = {7, 8}

u = odds.union(primes)
print(u)

i = odds.intersection(evens)
print(i)

i = odds.intersection(primes)
print(i)

d = odds.difference(primes)
print(d)

d = odds.symmetric_difference(primes)
print(d)

odds.update(primes)
print(odds)

odds.intersection_update(primes)
print(odds)

evens.difference_update(primes)
print(evens)

evens.symmetric_difference_update(primes)
print(evens)

print(setA.issubset(setB)) #//% False
print(setB.issubset(setA)) #//% True
print(setB.issuperset(setA)) #//% False
print(setA.issuperset(setB)) #//% True

print(setA.isdisjoint(setB)) #//% False
print(setA.isdisjoint(setC)) #//% True

#//% Copy
copy_setA = setA.copy()
also_copy_setA = set(setA)
print(also_copy_setA)

#//% Frozenset
fs = frozenset([1, 2, 3])
print(fs)
