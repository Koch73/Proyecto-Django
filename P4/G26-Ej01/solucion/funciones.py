import os
import pickle
import io
from clases import *


def validate_nros(inf, sup, mensaje = ""):
    x = int(input(mensaje))
    while inf > x or x > sup:
        x = int(input("error... Cargue un valor nuevamente entre {} y {} por favor".format(inf, sup)))
    return x

def validate_nombre(inf, sup, mensaje = ""):
    x = input(mensaje)
    while inf > len(x) or len(x) > sup:
        x = int(input("error... Cargue un valor nuevamente entre {} y {} por favor".format(inf, sup)))
    return x

def cargar_datos(FD):
    archivo = open(FD, "a+b")
    nuevo_socio = Socio()
    nuevo_socio.numero = validate_nros(0, 99999, "ingrese un numero positivo menor a 99999: ")
    nuevo_socio.nombre = validate_nombre(0, 40, "ingrese un nombre menor a 40 caracteres: ")
    nuevo_socio.plan = validate_nros(0, 3, "ingrese un numero positivo menor a 3: ")
    nuevo_socio.monto = round(float(input("ingrese el monto: ")), 2)
    pickle.dump(nuevo_socio, archivo)

    print("socio cargado satisfactoriamente")
    archivo.close()

def modificar_usuario(FD):
    archivo = open(FD, "a+b")
    codigo = validate_nros(0, 99999, "ingrese el codigo del usuario a cambiar: ")
    size = os.path.getsize(FD)
    archivo.seek(0,io.SEEK_SET)
    point = archivo.tell()

    while point < size:
        point = archivo.tell()
        socio = pickle.load(archivo)
        if codigo == socio.numero:
            socio.plan = validate_nros(0, 3, "ingrese un nuevo plan: ")
            socio.monto = round(float(input("ingrese un nuevo monto: ")), 2)
            archivo.seek(point, io.SEEK_SET)
            archivo.write(socio)
            archivo.close()
            return True

    archivo.close()
    return

def mostrar_archivo(FD):
    archivo = open(FD, "rb")
    size = os.path.getsize(FD)

    while archivo.tell() < size:
        print(pickle.load(archivo))

    archivo.close()
