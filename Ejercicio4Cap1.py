import math

radio = float(input("Ingrese el radio: "))

area = math.pi * radio**2
longitud = 2 * math.pi * radio

print(f"El area es: {area:.2f}")
print(f"La longitud es: {longitud:.2f}")