def gather_info():
    height = float(input("What is your height? (inches or meters) "))
    weight = float(input("What is your weight? (pounds or kilograms) "))
    unit = input("Are your measurements in metrics or imperial units? ").lower().strip()
    return (height, weight, unit)

def calculate_bmi(weight, height, unit='metric'):
    bmi = 0.0
    if unit == 'imperial':
        bmi = 703 * (weight / (height ** 2))
    elif unit.startswith('m'):
        bmi = (weight / (height ** 2))
        print(weight / (height ** 2))
    print("Your BMI is %s" % bmi)

while True:
    height, weight, unit = gather_info()
    if unit.startswith('i'):
        calculate_bmi(height=height, unit='imperial', weight=weight)
        break
    elif unit.startswith('m'):
        calculate_bmi(weight, height)
        break
    else:
        print("Error: Unknown measurement system. Please use imperial or metric")
