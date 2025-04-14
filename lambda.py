
#//% lambda arguments: expression
""" add10 = lambda x: x + 10
print(add10(5))

mult = lambda x, y: x * y
print(mult(2, 7)) """

from functools import reduce


points2D = [(1, 2), (15, 1), (5, -1), (10, 4)]
points2D_sorted = sorted(points2D, key=lambda point: point[1])
print(points2D_sorted)
points2D_sorted = sorted(points2D, key=lambda point: sum(point))
print(points2D_sorted)

#//% map
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
double_a = list(map(lambda x: x * 2, a))
print(double_a) # [2, 4, 6, 8, 10, 12, 14, 16, 18]

#//% filter
words = ["hemlock", "blood", "chemistry", "fluffy", "representation", "collision"]
words_length_gt7 = list(filter(lambda w: len(w) > 7, words))
print(words_length_gt7) # ['chemistry', 'representation', 'collision']

#//% reduce
b = [1, 2, 3, 4]
product_b = reduce(lambda x, y: x * y, b)
print(product_b)