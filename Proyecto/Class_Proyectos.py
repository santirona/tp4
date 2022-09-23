import os.path



class Proyectos:
    def __init__(self, usuario, descripcion, repositorio, actualizacion, lenguaje, likes, tags, url):
        self.usuario = usuario
        self.descripcion = descripcion
        self.repositorio = repositorio
        self.actualizacion = actualizacion
        self.lenguaje = lenguaje
        self.likes = likes
        self.tags = tags
        self.url = url



def cargar(apertura, arreglo, nombre_archivo):
    if not os.path.exists(nombre_archivo):
        print("\nNo existe el archivo...")
        return

    contador_registros_cargador = 0

    linea = apertura

    flag_primera = True

    while linea != "":
        if flag_primera:
            linea = apertura.readline()
            flag_primera = False
            continue

        linea = apertura.readline()
        registro = recorrer_archivo(linea)
        if registro.lenguaje != "":
            contador_registros_cargador += 1
            add_in_order(registro, arreglo)

    return(contador_registros_cargador)



def recorrer_archivo(linea):
    vector = [""] * 8
    contador = 0
    var = ""

    for i in linea:
        if i != "|":
            var += i

        else:
            vector[contador] = var
            var = ""
            contador += 1

    vector[5] = punto_flotante(vector[5])
    vector[6] = vectorizar(vector[6])

    return Proyectos(vector[0], vector[1], vector[2], vector[3], vector[4], vector[5], vector[6], vector[7])



def add_in_order(registro, vector):
    longitud = len(vector)

    posicion = longitud

    for i in range(longitud):
        if vector[i].repositorio > registro.repositorio:
            posicion = i
            break

    vector[posicion:posicion] = [registro]



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
