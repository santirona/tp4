import pickle
import os.path


class Populares():
    def __init__(self,mes,estrellas,cantidad):

        self.mes = mes
        self.estrellas = estrellas
        self.cantidad = cantidad


def guardar_populares(matriz,nombre_matriz):
    arreglo = []

    anterior = ''
    for i in range(len(matriz)):
        if anterior != i:
            archivo = open(nombre_matriz,'wb')
            for a in range(len(arreglo)):
                pickle.dump(arreglo[a])
            archivo.close()
            arreglo = []

        anterior = i
        for j in range(len(matriz[0])):
            if matriz[i][j] != 0:
                arreglo.append(Populares(i,j,matriz[i][j]))

def lectura_populares(nombre_matriz):
    array = []
    if not(os.path.exists(nombre_matriz)):
        print('El archivo no existe!!!!!')
        return

    largo = os.path.getsize(nombre_matriz)

    while nombre_matriz.tell() <= largo:
        file_objet = open(nombre_matriz,'rb')
        array.appen(pickle.load(file_objet))
        file_objet.close()





