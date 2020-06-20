go = True
while go:
    print("We're going")
    go = False
count = 0
while count < 10:
    print("we're counting")
    count += 1
count = 0
while count < 10:
    if count % 2 == 0:
        count += 1
        continue
    print("we're counting odd numbers %s" % count)
    count += 1
count = 0
while count < 10:
    if count % 2 == 0:
        break
    print("we're counting %s" % count)
    count += 1
colors = ['blue', 'green', 'red', 'purple']
for color in colors:
    print(color)
point = (2.1, 3.2, 7.6)
for value in point:
    print(value)
ages = { 'kevin': 59, 'bob': 40 }
for key in ages:
    print(key)
for key, value in ages.items():
    print(key)
    print(value)
print(ages.items())
key, value = ('bob', 40)
print(key)
print(value)
