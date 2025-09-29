#Creación de tpla vacia

tupla_vacia = ()

#Tupla con elementos int

tupla_numeros = (1, 2, 3, 4, 5)

#Tupla con cadenas

tupla_nombre = ("Christian", "Ana", "Luis", "Maria")

#Tupla con diferentes tipos de datos

tupla_mixta = (1, "Carlos", 12.5, 'z', False)

#Tuplas con un único elemento

tupla_unico_elemento = (3,)

#Acceder a los elementos de una tupla


print(frutas[1])
print(frutas[-2])

#Comprobación de la immutabilidad de las tuplas

#frutas[2] = "kiwi"  # Esto generará un error

#Desempaquetado de tuplas

persona = ("Carlos", 30, "Ingeniero")

nombre, edad, profesion = persona

print(nombre)
print(edad)
print(profesion)

#Métodos de tuplas

frutas = ("manzana", "banana", "cereza", "naranja", "uva", "manzana", "pera", "manzana", "cereza")

print("Método len: ")
print(len(frutas))

print("Método count: ")
print(frutas.count("manzana"))

print("Método index: ")
print(frutas.index("cereza"))