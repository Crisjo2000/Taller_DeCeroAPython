#Ejercicio práctico: Creación y gestión de tareas

tareas = []

def agregar_tarea(nombre, descripcion, prioridad):
    tarea = {
        "nombre": nombre,
        "descripcion": descripcion,
        "prioridad": prioridad,
        "completada": False
    }
    
    tareas.append(tarea)
    print(f"Tarea '{nombre}' agregada con éxito.")

def mostrar_tareas():
    if not tareas:
        print("No hay tareas por mostrar al momento.")
        return
    
    print("\nLista de Tareas:")
    for i, tarea in enumerate(tareas):
        estado ="completada" if tarea["completada"] else "pendiente"

        print(f"{i + 1}. {tarea['nombre']} - {tarea['descripcion']} (Prioridad: {tarea['prioridad']}) - Estado: {estado}")

        print (f"Descrpción: {tarea['descripcion']}")

def eliminar_tarea(indice):
    if 0 <= indice < len(tareas):
        tarea = tareas.pop(indice)
        print(f"Tarea '{tarea['nombre']}' eliminada")
    else:
        print("Indice inválido")

def marcar_completada(indice):
    if 0 <= indice < len(tareas):
        tareas[indice]['completada'] = True
        print(f"Tarea '{tareas[indice]['nombre']}' fue marcada como completada ")
    else:
        print("Indice no es válido")

def menu():

    while True:

        print("\nMenú de opcines de Gestión de Tareas")
        print("1. Agregar tarea")
        print("2. Mostrar tareas")
        print("3. Eliminar Tarea")
        print("4. Marcar tarea como completada")
        print("5. Salir")

        op = input("Selecione una opción (1-5): ")

        #Opción 1: Agregar Tarea

        if op == "1":
            nombre = input ("Ingrese el nombre de la tarea: ")
            descripcion = input ("Ingrese la descripción de la tarea: ")
            prioridad = input("Ingrese la prioridad de la tarea (Alta, Media, Baja): ")

            agregar_tarea(nombre, descripcion, prioridad)

        elif op == "2":
            mostrar_tareas()
        
        elif op == "3":

            mostrar_tareas()
            indice = int(input("Ingrese el número de la tarea que desee eliminar: ")) -1
            eliminar_tarea(indice)
        
        elif op == "4":
            mostrar_tareas()
            indice = int(input("Ingresa el número de la tarea que marcarás como completada: ")) - 1
            marcar_completada(indice)

        elif op == "5":
            print("Nos vemos!")
            break
        
        else:
            print("Opción inválida")

menu()