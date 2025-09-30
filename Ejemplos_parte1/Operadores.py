# Operadores aritméticos

a = 10
b = 3 

print("OPERADORES ARITMÉTICOS")
print("Suma:", a + b)          # Suma
print("Resta:", a - b)         # Resta
print("Multiplicación:", a * b) # Multiplicación
print("División:", a / b)      # División
print("División entera:", a // b) # División entera
print("Módulo:", a % b)        # Módulo
print("Exponenciación:", a ** b) # Exponenciación

# ---- Operadores de comparación

x = 5
y = 8

print("\nOPERADORES DE COMPARACIÓN")
print("Igual: ",  x == y )
print("No igual:", x != y)
print("mayor que: ", x >= y)
print("menor que ", x <= y)
print("mayor " , x > y)
print("menor ", x< y )

# --- Operadores lógicos

# and - Ambas condiciones debes ser verdaderas 

print("\nOPERADORES LÓGICOS")
print("AND")
print(True and True)    # True
print(True and False)   # False
print(False and True)   # False
print(False and False)  # False

# Or - Al menos una sde las condiciones deben de ser verdaderas

print("\nOR")
print(True or True)     # True
print(True or False)    # True
print(False or True)    # True
print(False or False)   # False

# Not - Invierte el valor de verdad 
print("\nNOT")
print(not False)    # True
print(not True)    # False

# Ejemplo usando variables 

edad = 20
tiene_licencia = True
 
puede_conducir = edad >=18 and tiene_licencia
print("\n¿Puede conducir?", puede_conducir)

