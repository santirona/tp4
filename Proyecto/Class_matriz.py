import pickle
import os.path
import os



class Populares():
    def __init__(self,mes,estrellas,cantidad):

        self.mes = mes
        self.estrellas = estrellas
        self.cantidad = cantidad

    def __str__(self):
        return str(self.mes) + '-' + str(self.estrellas) + '-' + str(self.cantidad)



def guardar_populares(matriz,nombre_matriz):
    arreglo = []
    registro = ''
    anterior = ''
    archivo = open(nombre_matriz,'wb')

    for i in range(len(matriz)+1):

        if anterior != i:
            for a in range(len(arreglo)):
              pickle.dump(arreglo[a],archivo)

            arreglo = []

        if i != 12:
            for j in range(len(matriz[0])):
                if matriz[i][j] != 0:
                    arreglo.append(Populares(i,j,matriz[i][j]))

        anterior = i

    archivo.close()



def lectura_populares(nombre_matriz):
    matriz = [[0]*5 for i in range(12)]

    array = []
    if not(os.path.exists(nombre_matriz)):
        print('El archivo no existe!!!!!')
        return

    largo = os.path.getsize(nombre_matriz)
    file_objet = open(nombre_matriz,'rb')

    while file_objet.tell() < largo:
        array.append(pickle.load(file_objet))

    file_objet.close()

    for i in range(len(array)):
        matriz[array[i].mes][array[i].estrellas] = array[i].cantidad

    mes_contador = 1

    print("Mes", "    Estrellas")
    print("\n	    🌟  🌟  🌟  🌟  🌟")

    for fila in matriz:
        if mes_contador < 10:
            print(mes_contador, " ",*fila, sep=" - ")
        else:
            print(mes_contador, "",*fila, sep=" - ")
        mes_contador += 1
