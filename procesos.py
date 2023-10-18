import os
import pickle
from typing import BinaryIO

from registro import *
def leer_csv(fd):
    v = []
    if not os.path.exists(fd):
        print('El archivo', fd, 'no existe')
    else:
        m = open(fd, 'rt')
        for linea in m:
            campos = linea.split(',')
            x = Invitado(campos[0], int(campos[1]), int(campos[2]), int(campos[3]))
            add_in_order(v, x)
        m.close()
    return v


def validar_entre(inf, sup, mensaje):
    num = int(input(mensaje))
    while num < inf or num > sup:
        num = int(input('Error! ' + mensaje))
    return num



def add_in_order(v, x):
    n = len(v)
    izq, der, pos = 0, n - 1, n
    while izq <= der:
        c = (izq + der)//2
        if v[c].nombre == x.nombre:
            pos = c
            break
        if x.nombre < v[c].nombre:
            der = c - 1
        else:
            izq = c + 1
    if izq > der:
        pos = izq
    v[pos:pos] = [x] #abre un espacio en lo que encontro y lo coloca ahi

#carga ordenada

def mostrar_vector(v):
    print("Listado de Invitados")
    for invitado in v:
        print(invitado)

def GenerarConteo(v):

    M = [[0]* 13 for _ in range(10)]
    for i in range(len(v)):
        f = v[i].ong
        c = v[i].mesa
        M[f][c] += 1
    return M
def mostrar_conteo(m):
    for f in range(len(m)):
        for c in range(len(m[f])):
            if m[f][c] > 1:
                print("mesa {} ong: {} cant. invitados: {}".format(f, c, m[f][c]))

def crear_archivo_ong(v, ong):
    fd = "Donaciones" + str(ong) + ".dat"
    m = open(fd , "wb")
    for invitado in v:
        if invitado.ong == ong:
            pickle.dump(invitado, m)
def promedio(suma, cantidad):
    promedio = 0
    if cantidad != 0:
        promedio  = (suma /cantidad)

def mostrarrecaudacion(ong):
    suma, cantidad  = 0, 0
    fd = "Donaciones" + str(ong) + ".dat"
    if not os.path.exists(fd):
        print("el archivo no existe...")
    else:
        m: BinaryIO = open(fd, "rb")
        size = os.path.getsize(fd)
        while m.tell() < size:
            invitado = pickle.load(m)
            print(invitado)
            suma += invitado.monto
            cantidad += 1
    m.close()

def guardar(v):
    ong = validar_entre(0, 9, "ingrese ong a buscar entre 0 y 9")
    crear_archivo_ong(v, ong)
