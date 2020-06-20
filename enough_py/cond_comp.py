this = "this"
test = "test"
one = 1
three = 3.0
true = True
false = False
print(1 < 2)
print(2 > 0)
print(2 == 1)
print("this" == this)
print("this" == "This")
print(3.0 >= three)
print(3.0 <= three)
print(3.1 <= three)
print(2 in [1, 2, 3])
print(4 in [1, 2, 3])
print(1 == one)
print(1 != 2)
print(1.0 == 1)
print(1.0 != 1)

if true:
    print("something is true")
if false:
    print("something is false")
name = "Kevin"
if len(name) >= 5:
    print("name is long")
else:
    print("name is short")
name = "Luke"
if len(name) >= 5:
    print("name is long")
elif len(name) == 4:
    print("name is average")
else:
    print("name is short")
if test:
    print("this is a test")
print(bool(test))
