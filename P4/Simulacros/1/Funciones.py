import os
import random
import io
import pickle
from Clases import*

def add_in_order(v,x):
    left, right, pos = 0, len(v), len(v)-1

    while left < right:
        c = (left + right) // 2

        if v[pos].titulo == x.titulo:
            pos = c
            break

        elif x.titulo > v[c].titulo:
            left = c + 1
        elif x.titulo < v[c].titulo:
            right = c - 1
    if left > right:
        pos = left
    v[pos:pos] = [x]


def cargar_datos(n):
    titulos = "Jurasic Park", "El rey leon", "La sirenita"
    v = []
    for i in range(n):
        v.append(Pelicula())

        v[i].titulo = random.choice(titulos)
        v[i].id = random.randint(1000000,9999999)
        v[i].tipo = random.randint(0,9)
        v[i].importe = round(random.uniform(1,90000),2)
        v[i].pais = random.randint(0,19)

        add_in_order(v, v[i])
    return v


def mostrar_peliculas(v):
    for i in range(len(v)):
        print(v[i])
