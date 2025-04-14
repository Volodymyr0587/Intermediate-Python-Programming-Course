import pprint

employee1 = {"name": "John Doe", "age": 35, "job_title": "manager"}
print(employee1)

employee2 = dict(name="Mary", age=42, job_title="accountant")
print(employee2)

employee1_name = employee1["name"]
print(employee1_name) 

# employee1_lastname = employee1["lastname"] #//! KeyError
employee1_lastname = employee1.get("lastname") #//* None
print(employee1_lastname)

employee1["email"] = "john@doe.com"
employee1["salary"] = 15000
pprint.pprint(employee1, indent=4, width=20)

del employee1["salary"]
pprint.pprint(employee1, indent=4, width=20)

email = employee1.pop("email")
pprint.pprint(employee1, indent=4, width=20)

last_item = employee1.popitem()  #//*  removes the item that was last inserted into the dictionary
pprint.pprint(employee1, indent=4, width=20)

for key in employee2:
    print(f"{key} -- {employee2[key]}")
    
for key in employee2.keys():
    print(key)
    
for value in employee2.values():
    print(value)
    
for key, value in employee2.items():
    print(f"{key} -- {value}")
    
    
employee1_copy = employee1.copy()
# employee1_copy = dict(employee1)
employee1_copy["address"] = "Some Street, 55"
print(employee1)
print(employee1_copy)

words_length1 = {"sun": 3, "water": 5}
words_length2 = {"water": "5", "apple": 5, "pear": 4}

words_length1.update(words_length2)
print(words_length1)

blue_hex_rgb = ('#0000FF', '0,0,255')
colors = {blue_hex_rgb: "blue"}
print(colors)