a = 'a'
zero = 0
one = 1
two = 2
empty = {}
print(not 1)
print(bool(1))
print(not True)
if not len("something") > 10:
    print("it's not")
print('a' == a)
print(1 == one)
print({} == empty)
print(1 == 1.0)
print(id(1))
print(id(1.0))
print(one and 2)
print(zero and 1)
print(bool(0))
var = None
print(var and str(var))
var = 1
print(var and str(var))
print(1 and 2 and zero and 3)
print(one or 2)
print(zero or 2)
var = None
other_var = var or "default"
print(other_var)
var = "1"
other_var = var or "default"
print(other_var)
print(0 or {} or two or True)
