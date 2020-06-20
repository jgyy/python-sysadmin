with open('xmen.txt', 'a') as xmen_file:
    xmen_file.write("Professor Xavier\n")

with open('xmen.txt') as xmen_file:
    print(xmen_file.read())
