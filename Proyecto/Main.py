from Class_Proyectos import *
from Class_matriz import *
from datetime import datetime
import os.path
import os
import pickle



def buscador_meses(proyecto):
    if proyecto.actualizacion[5] == 0:
        mes = proyecto.actualizacion[6]
        return mes

    else:
        mes = proyecto.actualizacion[5] + proyecto.actualizacion[6]
        return mes



def popularidad(vector):

    matriz = [[0]*5 for i in range(12)]

    for i in range(len(vector)):
        matriz[int(buscador_meses(vector[i])) - 1][int(representacion(vector[i].likes)) - 1] += 1

    m = int(input("\nIngrese un mes que desee ver la totalidad de sus proyectos: "))

    while m < 1 or m > 12:
        m = int(input("\nERROR! ese mes no existe. Ingrese un mes que desee ver la totalidad de sus proyectos: "))

    acumulador = 0
    m = m - 1

    for i in range(5):
        acumulador += matriz[m][i]

    mes_contador = 1

    print("Mes", "    Estrellas")
    print("\n	    🌟  🌟  🌟  🌟  🌟")

    for fila in matriz:
        if mes_contador < 10:
            print(mes_contador, " ",*fila, sep=" - ")
        else:
            print(mes_contador, "",*fila, sep=" - ")
        mes_contador += 1

    print("\nEl total de proyectos actualizados en el mes que selecciono es:", acumulador)

    return matriz



def lenguajes(vector):

    array_lenguaje = []
    contador = []

    for i in range(len(vector)):
        if vector[i].lenguaje not in array_lenguaje:
            array_lenguaje.append(vector[i].lenguaje)
            contador.append(1)

        else:
            for j in range(len(array_lenguaje)):
                if vector[i].lenguaje == array_lenguaje[j]:
                    contador[j] += 1

    for i in range(len(contador) - 1):
        for j in range(i + 1, len(contador)):
            if contador[i] < contador[j]:
                contador[i], contador[j] = contador[j], contador[i]
                array_lenguaje[i], array_lenguaje[j] = array_lenguaje[j], array_lenguaje[i]

    print("\nLos lenguajes de programacion son:")

    for i in range(len(array_lenguaje)):
        print("\n",array_lenguaje[i],":",contador[i])



def filtrar_por_tag(vector):

    tag = input("\nIngrese la tag para filtrar los proyectos con esta: ")
    print("")

    for i in range(len(vector)):
        if tag in vector[i].tags:
            print(f"Repositorio: {vector[i].repositorio :<35}"
                  f"Fecha: {vector[i].actualizacion :<20}"
                  f"Estrella/s: {representacion(vector[i].likes) :<15}")

    opcion = input("\n¿Desea almacenar almacenar este listado? S/N: ")

    return opcion, tag



def guardar_filtrados(vector, tag, archivo):

    linea = None

    apertura = open(archivo, mode="wt")

    apertura.write("nombre_usuario|repositorio|fecha_actualizacion|lenguaje|estrellas|tags|url\n")

    for i in range(len(vector)):
        pos = vector[i]

        if tag in pos.tags:
            linea = str(pos.usuario) + "|" + str(pos.repositorio) + "|" + str(pos.actualizacion) + "|"\
            + str(pos.lenguaje) + "|" + str(pos.likes) + "k|" + str(pos.tags) + "|" + str(pos.url) + "\n"

            apertura.write(linea)

    apertura.close()



def representacion(likes):

    likes = float(likes)

    if likes > 40:
        return 5

    estrellas = -1
    contador = 0

    while estrellas != 0:
        contador += 10

        if likes - contador <= 0:
            string = str(contador)
            return string[0]



def busqueda_proy_rep(array, variable):

    izq = 0
    der = len(array) - 1
    pos = 0
    while izq <= der:
        pos = (izq+der)// 2
        if variable == array[pos].repositorio:
            return pos

        if variable < array[pos].repositorio:
            der = pos - 1
        else:
                izq = pos + 1
    return -1



def actualizar_proyecto(array,pos):
    array[pos].url = input('Ingrese la nueva URL: ')
    aux = datetime.now()

    if len(str(aux.month)) == 1:
        mes = '0' + str(aux.month)
    else:
        mes = str(aux.month)

    array[pos].actualizacion = str(aux.year) + '-' + mes + '-' + str(aux.day)



def menu():

    array_proyectos = []

    nombre_archivo = "proyectos.csv"
    nombre_tags = "tags.dat"
    nombre_matriz = 'martriz.dat'

    opciones = ("1", "2", "3", "4", "5", "6", "7", "8")

    menu1 = '\n1) Cargar proyectos\n2) Filtrar por tag\n3) Cantidad de proyectos por lenguaje\n4) Popularidad mensual'
    menu2 = '\n5) Buscar un proyecto actualizado\n6) Guardar proyectos populares\n7) Mostrar archivos populares\n8) Salir del programa'

    opcion = 0

    flag_4 = False



    while opcion != "8":

        if opcion == "1":
            registros_cargados, registros_no_cargados = cargar(array_proyectos, nombre_archivo)
            print("\nLa cantidad de registros cargados fue de: ", registros_cargados)
            print("\nLa cantidad de registros NO cargados fue de: ", registros_no_cargados)

        elif opcion == "2":
            opcion, tag = filtrar_por_tag(array_proyectos)
            if opcion == "S" or opcion == "s":
                guardar_filtrados(array_proyectos, tag, nombre_tags)

        elif opcion == "3":
            lenguajes(array_proyectos)

        elif opcion == "4":
            matriz_popularidad = popularidad(array_proyectos)
            flag_4 = True

        elif opcion == "5":
            repositorio = input('Ingrese el repositorio que quiere busacar: ')
            posicion = busqueda_proy_rep(array_proyectos,repositorio)

            if posicion != -1:
                actualizar_proyecto(array_proyectos,posicion)
            else:
                print('El proyecto no existe!!!!')

        elif opcion == "6":
            if flag_4:
                guardar_populares(matriz_popularidad, nombre_matriz)
            else:
                print("Primero debe crear la matriz en la opcion 4.")

        elif opcion == "7":
            lectura_populares(nombre_matriz)

        print("\n","*" * 40, '¡Bienvenido al menú de opciones!', "*" * 40,"\n", menu1, menu2)

        opcion = input("\nIngrese la opcion del menu que desea: ")

        while opcion not in opciones:
            print("\n","*" * 40, '¡Bienvenido al menú de opciones!', "*" * 40,"\n", menu1, menu2)
            opcion = input("\nERROR! ingrese una opcion correcta del menu por favor: ")



def main():
    menu()



if __name__ == '__main__':
    main()


