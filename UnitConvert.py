import sys

factors = {
    ('mm', 'cm'): 0.1,
    ('cm', 'mm'): 10,
    ('cm', 'm'): 0.01,
    ('m', 'cm'): 100
}

def convert(unit_from, unit_to, value):
    if (unit_from, unit_to) in factors:
        factor = factors[(unit_from, unit_to)]
        return value * factor
    else:
        print("Unsupported Conversion!")
        sys.exit(1)

def help():
    print("Unit Converter Program")
    print("Usage: python3 convert.py [unit_from] [unit_to] [value]")
    print("Example: python3 convert.py mm cm 30")
    print("Supported conversions:")
    for (unit_from, unit_to), factor in factors.items():
        print(f"{unit_from} -> {unit_to}")

if len(sys.argv) == 2 and sys.argv[1] == "help":
    help()
    sys.exit(0)

if len(sys.argv) != 4:
    print("Error: Incorrect number of arguments.")
    help()
    sys.exit(1)

unit_from = sys.argv[1]
unit_to = sys.argv[2]

try:
    value = float(sys.argv[3])
except ValueError:
    print("Error: Value must be a number.")
    sys.exit(1)

result = convert(unit_from, unit_to, value)
print(f"{value} {unit_from} is {result} {unit_to}")
