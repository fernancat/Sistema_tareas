from io import open

def agregar_tarea(*tareas):
    fichero = open('tareas.txt','a')

    for i in tareas:
        fichero.write(i + " \n") #escribir texto



def listar_tareas():
    indice = 1
    with open('tareas.txt','r') as fichero:
        print("-----------TAREAS POR HACER-----------")
        for i in fichero:
            print(f" {indice}.{i.strip()}")
            indice+=1
        print("-------------------------------------")

    #tareas_completadas
    indice = 1
    with open('tareas_completadas.txt','r') as fichero2:
        print("-----------TAREAS COMPLETADAS-----------")
        for e in fichero2:
            print(f" {indice}.{e.strip()}")
            indice += 1
        print("-------------------------------------")

def marcar_completado():
    fichero = open('tareas.txt','r+')

    lineas = fichero.readlines()

    tarea = int(input("Ingresa el numero de la tarea que deseas borrar: "))

    fichero2 = open('tareas_completadas.txt','a')

    fichero2.write(lineas[tarea-1])
    del(lineas[tarea-1])

    fichero.seek(0)
    fichero.writelines(lineas)




numero_tareas = int(input("Ingresa el numero de tareas que agregaras: "))
for i in range (numero_tareas):
    agregar_tarea(input("Escriba una tarea: "))

listar_tareas()


marcar_completado()