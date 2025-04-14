
#//% Strings: ordered, immutable, text representation

my_string = "Hello World"
print(my_string)

char = my_string[0]
print(char)

substring = my_string[2:5]
print(substring)

reverse_string = my_string[::-1]
print(reverse_string)

#//% Concat strings
greeting = "Hello"
name = "Tom"
sentence = greeting + " " + name
print(sentence)

for ch in greeting:
    print(ch)
    
if 'e' in greeting:
    print("YES")
else:
    print("NO")
    
    
my_string = "    Hello World"
my_string = my_string.strip()
print(my_string)


my_string = "Hello World"
print(my_string.upper())
print(my_string.lower())
print(my_string.startswith("H"))
print(my_string.endswith("d"))
print(my_string.find("o"))
print(my_string.count("o"))
print(my_string.replace("World", "Universe"))


my_string = "how are you doing"
words = my_string.split()
print(words)

my_string = "how,are,you,doing"
words = my_string.split(",")
print(words)
print(" ".join(words))


#//% FORMAT STRINGS  (%, .format(), f-Strings)

#//*  %
name = "Tom"
age = 34
height = 1.823
my_string = "the name is %s age %d height %.2f" % (name, age, height)
print(my_string)

#//*  .format
my_string =  "the name is {} age {} height {:.2f}".format(name, age, height)
print(my_string)

#//*  f-String
my_string =  f"the name is {name} age {age} height {height:.2f}"
print(my_string)


