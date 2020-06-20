with open('./script_py/xmen.txt', 'a') as xmen_file:
    xmen_file.write("\nProfessor Xavier\n")

with open('./script_py/xmen.txt') as xmen_file:
    print(xmen_file.read())
