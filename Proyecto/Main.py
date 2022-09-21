




def menu():

    arr_proyectos = []

    opciones = ("1", "2", "3", "4", "5", "6", "7", "8")

    menu1 = '\n1) Cargar proyectos\n2) Filtrar por tag\n3) Cantidad de proyectos por lenguaje\n4) Popularidad mensual'
    menu2 = '\n5) Buscar un proyecto actualizado\n6) Guardar proyectos populares\n7) mostrar archivos populares\n8) Salir del programa'

    opcion = 0

    while opcion != "8":

        if opcion == "1":
            pass

        elif opcion == "2":
            pass

        elif opcion == "3":
            pass

        elif opcion == "4":
            pass

        elif opcion == "5":
            pass

        elif opcion == "6":
            pass

        elif opcion == "7":
            pass

        print("\n","*" * 40, '¡Bienvenido al menú de opciones!', "*" * 40,"\n", menu1, menu2)

        opcion = input("\nIngrese la opcion del menu que desea: ")

        while opcion not in opciones:
            print("\n","*" * 40, '¡Bienvenido al menú de opciones!', "*" * 40,"\n", menu1, menu2)
            opcion = input("\nERROR! ingrese una opcion correcta del menu por favor: ")



def main():
    menu()

if __name__ == '__main__':
    main()
