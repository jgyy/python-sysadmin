ages = { 'kevin': 59, 'alex': 29, 'bob': 40 }
print(ages)
print(ages['kevin'])
print(ages['bob'])
ages['kayla'] = 21
print(ages)
ages['kevin'] = 60
print(ages)
del ages['bob']
print(ages)
del ages
ages = { 'kevin': 50, 'alex': 20 }
print(ages)
print(ages.pop('alex'))
print(ages)
my_dict = { 1: 'this', 1.2: 'that', 'keith': 'Thomson' }
print(my_dict)
print(my_dict[1.2])
print(ages)
ages = { 'kevin': 50, 'alex': 20, 'kayla': 21 }
print(ages)
print(ages.values())
print(ages.keys())
print(ages.items())
weights = dict(kevin=60, bob=240)
print(weights)
colors = dict([('kevin', 'green'), ('bob', 'blue')])
print(colors)
