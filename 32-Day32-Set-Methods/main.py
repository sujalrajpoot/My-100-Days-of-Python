s1, s2 = {1,2,3,4}, {1,2,3,4,5,6}
print('S1 Intersection:',s1.intersection(s2))

s1.update(s2)
print('S1 Update:',s1)

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities3 = cities.union(cities2)
print('S1 Intersection:',cities3)

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities.update(cities2)
print('cities update:',cities)

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities3 = cities.intersection(cities2)
print('cities3 intersection:',cities3)

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities.intersection_update(cities2)
print('cities intersection update:',cities)

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities2.intersection_update(cities)
print('cities2 intersection update:',cities2)

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities3 = cities.symmetric_difference(cities2)
print('cities3 symmetric_difference:',cities3)

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities.symmetric_difference_update(cities2)
print('cities symmetric_difference_update:',cities)

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Seoul", "Kabul", "Delhi"}
print('cities difference:',cities.difference(cities2))

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
print('cities isdisjoint:',cities.isdisjoint(cities2))

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Seoul", "Kabul"}
print('cities isdisjoint:',cities.isdisjoint(cities2))

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Seoul", "Kabul"}
print('cities2 issuperset:',cities.issuperset(cities2))
cities3 = {"Seoul", "Madrid","Kabul"}
print('cities3 issuperset:',cities.issuperset(cities3))
print('cities3 issuperset:',cities3.issuperset(cities2))

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Delhi", "Madrid"}
print('cities2 issubset:',cities2.issubset(cities))

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.add("Helsinki")
print('cities add:',cities)

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Helsinki", "Warsaw", "Seoul"}
cities.update(cities2)
print('cities update:',cities)

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.discard("Tokyo")
print('cities discard:',cities)

cities = {"Tokyo", "Madrid", "Berlin", "Delhi", "Seoul"}
cities.remove("Seoul")
print('cities remove:',cities)

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
print('before pop cities:',cities)
item = cities.pop()
print('after pop cities:',cities)
print('cities poped:',item)

# cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# del cities
# print(cities) # NameError: name 'cities' is not defined.

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.clear()
print('cities clear:',cities)

info = {"Carla", 19, False, 5.9}
if "Carla" in info:
    print("Carla is present.")
else:
    print("Carla is absent.")