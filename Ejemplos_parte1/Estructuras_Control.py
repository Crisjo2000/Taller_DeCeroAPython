# Estructuras de Control

# Estructuras condicionales: if, elif, else

#estructura basica 

edad = 17 
print("Resultado if 1 ")

if edad >= 18:
    print("Eres mayor de edad"  )
else: 
    print("eres menor de edad" )

# Múltiples condiciones con elif

nota = 85 

print("\nResultado if 2 ")

if nota >= 90:
    print("Excelente")
elif nota >= 80 : 
    print("Muy bien")
elif nota >= 70:
    print("Bien")
elif nota >= 60:
    print("Suficiente")
else: 
    print("Insuficiente")


# If anidado 

tiempo = "soleado"
temperatura = 25

if tiempo == "soleado":
    if temperatura > 20:
        print("Perfecto para ir a la playa")
    else:
        print("Soleado pero frío")
else:
    print("No es un buen día para salir")


# Bucles 
# # Estructuras de repetición: for, while
#Bucle for 

print("\nBucle for")

print()
print("Bucle contando de 0 a 4")
for i in range(5):
    print("Iteración", i)

frutas = ["manzana", "banana", "orange"]

print("\nBucle recorriendo una lista de frutas")
for aux in frutas :
    print("Fruta:", aux) 

print("\nBucle recorriendo una cadena de texto")
for letra in "Python":
    print("Letra:", letra)

# Bucle while 

print("\nBucle while")
contador = 0

while contador < 5:
    print("Contador:", contador    )    
    contador +=1



# While con condición más compleja
numero = 1
while numero <= 100:
    if numero % 2 == 0:  # Si es par
        print(f"{numero} es par")
    numero += 1



# Uso del break y continue 

print("\nUso de break y continue")
print("Bucle con break")
for i in range(10):
    if i == 5:
        break
    print("Iteración", i)

# continue  - SAlta a la sigunete iteración
print("\nBucle con continue")
for i in range(10):
    if i % 2== 0  :
        continue
    print("Iteración", i)
else:
    print("Bucle terminado")
    




