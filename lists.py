mylist = ["banana", "cherry", "apple"]
print(mylist)

item = mylist[-1]
print(item)

for i in mylist:
    print(i)
    
if "banana" in mylist:
    print("YES")
    
print(len(mylist))

mylist.append("lemon")
print(len(mylist))
print(mylist)

mylist.insert(1, "blueberry")
print(mylist)

item = mylist.pop()
print(item)
print(mylist)

item = mylist.remove("cherry")
print(mylist)

# mylist.clear()
# print(mylist)

mylist.reverse()
print(mylist)

mylist.sort()
print(mylist)

mylist.sort(key=lambda x: x[2])
print(mylist)

numbers = [4, 3, 1, -1, -5, 10]
numbers.sort(key=lambda x: x % 2 == 0)
print(numbers)

new_list = sorted(mylist)
print(mylist, new_list)

zeros = [0] * 5
print(zeros) # [0, 0, 0, 0, 0]

numbers = [1, 2, 3, 4, 5]
new_numbers = zeros + numbers
print(new_numbers) # [0, 0, 0, 0, 0, 1, 2, 3, 4, 5]


for_slice = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
a = for_slice[1:5]
b = for_slice[:5]
c = for_slice[1:]
print(a, b, c)
print(for_slice[::2])
print(for_slice[::-1])


list_original = ["metallica", "iron maiden", "judas priest"]
list_copy = list_original.copy()
list_copy = list(list_original)
list_copy = list_original[:]

list_copy.append("blind guardian")
print(list_original, list_copy, sep="\n")


even = [n for n in range(10) if n % 2 == 0]
odd = [n for n in range(10) if n % 2 != 0]
print(even, odd, sep="\n")

squared_even = [n ** 2 for n in even]
print(squared_even)