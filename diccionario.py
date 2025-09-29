#Diccionario vacío

diccionario_vacio = {}

#Diccionario con datos

estudiante = {
    "nombre": "Carlos",
    "edad": 21,
    "carrera": "Ingeniería",
    "nota": 8.5,
    "aprobado": True
}

#Acceso a los elementos del diccionario

print(estudiante["nombre"])
print(estudiante["nota"])

#Error de clave no encontrada dentro de nuestro diccionario

print(estudiante["seccion"])

#Modificar y agregar elementos

estudiante["nota"] = 7
estudiante["curso"] = "Matemáticas"

print(estudiante)

#Eliminación de elementos

del estudiante["aprobado"]
print(estudiante)

print(estudiante.pop("edad"))
print(estudiante)

estudiante.clear()
print(estudiante)

#Recorrido de un diccionario

#Recorrido por claves

for clave in estudiante:
    print(clave)

#Recorrido por valores

for valor in estudiante.values():
    print("a")
    print(valor)

#Recorrido por claves y valores
for clave, valor in estudiante.items():
    print(f"{clave}: {valor}")