#Tipo de datos en Python

# ------ Numeros  --------

# Enteros

numero_entero = 42
negativo = -15

# Flotentes (decimales)

numero_decimal = 3.14
precio = 19.99

# operaciones basicos 

suma = 10 + 5
resta = 10-5
multiplicacion = 10 * 5
division = 15/3
division_entera = 15 // 2
modulo = 20/5 
potencia = 2 ** 3

# Operaciones con variables 

suma_var = numero_entero + numero_decimal
resta_var = precio - numero_decimal 


print("Suma:", suma)
print("Resta:", resta)
print("Multiplicacion:", multiplicacion)
print("Division:", division)
print("Division entera:", division_entera)
print("Modulo:", modulo)
print("Potencia:", potencia)

print("Suma con variables:", suma_var)
print("Resta con variables:", resta_var)

# ------ Cadenas de texto (Strings)  --------

Nombre = "Carlos"
apellido  = "Gonzalez"
mensaje = """ es texto es 
de multiples 
lineas 
"""

# Operaciones con cadenas 

# Concatenacion -->
Saludo = "hola " +  Nombre
repetir = "Python " * 3

# Metodos utiles de las cadenas 
mayuscula = Nombre.upper()
minuscula = apellido.lower()
longitud = len(Nombre)

print ()
print("------ parte de cadenas ------")

print("Saludo:", Saludo)
print("Repetir cadena:", repetir)
print("mayuscula:", mayuscula)
print(apellido.lower() , " texto en minuscula ")
print("Longitud del nombre:", longitud)

#------ Variables Booleanos  --------

verdadero = True 
falso = False

# comparaciones (operaciones relacionales)

mayor =  10 > 5
menor = 3 < 7
igual = 5 == 5

print()
print("------ parte de booleanos ------")
print("Valor verdadero:", verdadero)
print("Valor falso:", falso)
print("10 es mayor que 5:", mayor)
print("3 es menor que 7:", menor)
print("5 es igual a 5:", igual)


# ----- Parte de Listas(array) --- 

frutas = ["manzana", "banana", "cereza"]
numeros = [ 1, 2, 3, 4, 5]
mixta = ["texto", 42, True, 3.14]

print(frutas[1]) # banana 
print(numeros[0]) # 1
print(mixta[2]) # True

print()
print("Listas iniciales: ")
print("Lista de frutas:", frutas)
print("Lista de numeros:", numeros)
print("Lista mixta:", mixta)

# mODIFICAR ELEMENTOS
frutas.append("naranja") # Agregar al final
numeros.remove(5) # Eliminar elemento 
mixta.insert(1, "nuevo") # Insertar en posicion 1
print()
print("Listas despues de las modificaciones: ")
print("Lista de frutas:", frutas)
print("Lista de numeros:", numeros)
print("Lista mixta:", mixta)












