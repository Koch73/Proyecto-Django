from clases import *
from funciones import *

def menu():
    print("-"*30)
    print("opcion 1")
    print("opcion 2")
    print("opcion 3")
    print("opcion 4")
    print("opcion 5")
    print("opcion 6")
    print("opcion 0 (salir)")
    print("-"*30)


def main():
    menu()
    opc = int(input("ingrese una opcion: "))
    FD = "socios.dat"
    while opc != 0:

        if opc == 1:
            cargar_datos(FD)
        if opc == 2:
            r = modificar_usuario(FD)
            if not r:
                print("El usuario no se ha encontrado. Intente nuevamente...")
        if opc == 3:
            pass
        if opc == 4:
            mostrar_archivo(FD)
        if opc == 5:
            pass
        if opc == 6:
            pass

        opc = int(input("ingrese una opcion: "))

if __name__ == "__main__":
    main()
