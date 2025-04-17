import copy

#% - shallow copy: one level deep, only references of nested child objects
#% - deep copy: full independent copy

#? shallow copy
org = [0, 1, 2, 3, 4]
# cpy = copy.copy(org)
# cpy = org.copy()
# cpy = list(org)
cpy = org[:]
cpy[0] = -10
print(cpy) # [-10, 1, 2, 3, 4]
print(org) # [0, 1, 2, 3, 4]


#? deep copy
org = [[0, 1, 2, 3, 4], [5, 6, 7, 8, 9]]
cpy = copy.deepcopy(org)
cpy[0][0] = -10
print(cpy) # [[-10, 1, 2, 3, 4], [5, 6, 7, 8, 9]]
print(org) # [[0, 1, 2, 3, 4], [5, 6, 7, 8, 9]] 


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
     
class Company:
    def __init__(self, boss, employee):
        self.boss = boss
        self.employee = employee 

""" p1 = Person("Alex", 27)
p2 = copy.copy(p1)

p2.age = 55

print(p2.age) # 55
print(p1.age) # 27 """
 
p1 = Person('Alex', 55)
p2 = Person('Joe', 27)

""" company = Company(p1, p2)
company_clone = copy.copy(company)
company_clone.boss.age = 56
print(company_clone.boss.age) # 56
print(company.boss.age) # 56 """

company = Company(p1, p2)
company_clone = copy.deepcopy(company)
company_clone.boss.age = 56
print(company_clone.boss.age) # 56
print(company.boss.age) # 55