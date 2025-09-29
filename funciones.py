#función sin parámetros ni retorno

def sonido_gato():
    print("Miau!!!")

sonido_gato()

#funciones con parámetros pero sin retornos

def saludar(nombre):
    print(f"Hola {nombre}, ¿cómo estás?")

saludar("Christian")
saludar("Luisa")

#Funciones con parámetros y retornos

def sumar(a, b):
    resultado = a + b
    return resultado

suma = sumar(4, 2)
print(suma)

#Funciones con múltiples parámetros

def presentar(nombre, edad, carrera):
    return f"Hola, mi nombre es {nombre}, tengo {edad} años y estudio {carrera}."

print(presentar("Christian", 24, "Ingeniería en Sistemas"))


#Funciones con múltiples variables de retorno

def operaciones(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b

    return suma, resta, multiplicacion, division

s, r, m, d = operaciones(4, 3)

print(f"Suma: {s}, Resta: {r}, Multiplicación: {m}, División: {d}")


#Ámbito de las variables

#variable Global
nombre_global = "Christian"

def mostrar_nombre():

    #Variable local
    nombre_local = "Josué"

    print("Dentro de la función: ")
    print("Nombre Global: ", nombre_global)
    print("Nombre Local: ", nombre_local)

mostrar_nombre()

print("Fuera de la función: ")
print("Nombre Global: ", nombre_global)
#print("Nombre Local: ", nombre_local)  # Esto generará un error