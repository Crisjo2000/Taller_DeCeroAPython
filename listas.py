#Creación de listas

#Lista vacia

lista_vacia = []

#Lista con elementos

Lista_numeros = [1, 2, 3, 4, 5]

#Lista con diferentes tipos de datos

Lista_mixta = [1, "Christian", 3.1415, 'a', True]

#Acceso a los elementos de una lista

#            -4       -3       -2        -1                      
#            0        1        2         3
colores = ["rojo", "verde", "azul", "amarillo"]

print (colores[2])

print (colores[-3])

#Modificar los elementos de una lista

colores[0] = "rosado"

print (colores)

#Operaciones y métodos de las listas

#APPEND

colores.append("naranja")
print(colores)

#INSERT

colores.insert(1, "verde lima")
print(colores)

#REMOVE

colores.remove("verde")
print(colores)

#POP

print(colores.pop())
print(colores)

#SORT

colores.sort()
print(colores)

#REVERSE

colores.reverse()
print(colores)

#LEN

print(len(colores))

#CLEAR

colores.clear()
print(colores)


#Recorrido de listas

lista_nueva = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

for num in lista_nueva:
    print(num)

