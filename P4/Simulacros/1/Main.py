from Funciones import *
from Clases import *

def menu():
    print("-"*40)
    print("opcion 1")
    print("opcion 2")
    print("opcion 3")
    print("opcion 4")
    print("opcion 5")
    print("opcion 6")
    print("opcion 7")
    print("opcion 0: salir")
    print("-"*40)


def main():
    menu()
    opc = int(input("seleccione una opcion:"))
    while opc != 0:

        if opc == 1:
            v = cargar_datos(20)
        elif opc == 2:
            mostrar_peliculas(v)
        elif opc == 3:
            pass
        elif opc == 4:
            pass
        elif opc == 5:
            pass
        elif opc == 6:
            pass
        elif opc == 7:
            pass
        opc = int(input("seleccione una opcion:"))



if __name__ == "__main__":
    main()
