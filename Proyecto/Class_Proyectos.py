import os.path
import os


class Proyectos:
    def __init__(self, usuario, repositorio, actualizacion,
                 lenguaje, likes, tags, url):

        self.usuario = usuario
        self.repositorio = repositorio
        self.actualizacion = actualizacion
        self.lenguaje = lenguaje
        self.likes = likes
        self.tags = tags
        self.url = url


    def __str__(self):
        tags = ''
        for i in self.tags:
            tags += i

        return self.usuario + '-' + self.repositorio + '-' +\
        '-' + self.actualizacion + '-' + self.lenguaje + '-' +\
        '-' + str(self.likes) + '-' + tags + self.url


def cargar(arreglo, nombre_archivo):

    if not os.path.exists(nombre_archivo):
        print("\nNo existe el archivo...")
        return

    linea = None
    cont_registros_cargados = 0
    cont_registros_no_cargados = 0



    flag_primera = True

    apertura = open(nombre_archivo, mode="rt", encoding="utf8")

    while linea != "":

        if flag_primera:
            linea = apertura.readline()
            flag_primera = False
            continue

        linea = apertura.readline()
        if linea == '':
            continue
        registro = recorrer_archivo(linea)

        if registro.lenguaje != "":

            repetido = buscar_repetidos(registro.repositorio, arreglo)

            if not repetido:
                cont_registros_cargados += 1
                add_in_order(registro, arreglo)

            else:
                cont_registros_no_cargados += 1

        else:
            cont_registros_no_cargados += 1

    apertura.close()

    return cont_registros_cargados, cont_registros_no_cargados



def recorrer_archivo(linea):

    control = ('|','\n','')
    flag = False
    vector = [''] * 7
    contador = 0
    var = ''

    for i in linea:
        if not(i in control):
            var += i

        else:
            if contador == 2:
                flag = True
                contador += 1
                continue
            if flag:
                vector[contador-1] = var
                var = ''
            else:
                vector[contador] = var
                var = ''

            contador += 1

    vector[4] = punto_flotante(vector[4])
    vector[5] = vectorizar(vector[5])

    return Proyectos(vector[0], vector[1], vector[2], vector[3], vector[4], vector[5], vector[6])



def add_in_order(registro, vector):
    n = len(vector)
    izq,der = 0, n-1
    pos = n

    while izq <= der:
        c = (izq+der) // 2
        if registro.repositorio == vector[c].repositorio:
            pos = c
            break
        if registro.repositorio < vector[c].repositorio:
            der = c - 1
        else:
            izq = c + 1
    if izq > der:
        pos = izq

    vector[pos:pos] = [registro]



def punto_flotante(string):

    if string == "":
        valor_flotante = 0
        return valor_flotante

    valor_flotante = ""

    for i in range(len(string)):
        if string[i] == "k" or string[i] == "K":
            break

        valor_flotante += string[i]

    float(valor_flotante)

    return valor_flotante



def vectorizar(cadena):

    vector = []

    longitud = len(cadena)

    if longitud == 0:
        return vector

    var = ""

    for i in range(longitud):
        if cadena[i] == ",":
            vector.append(var)
            var = ""
            continue

        var += cadena[i]

        if longitud - 1 == i:
            vector.append(var)

            return vector



def buscar_repetidos(repositorio, vector):

    for i in range(len(vector)):
        if vector[i].repositorio == repositorio:
            return True

    return False
