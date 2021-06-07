# -*- coding: utf-8 -*-
"""
Created on Sat May 15 22:43:26 2021

@author: cesar
"""

"""Practica Algoritmos Geneticos"""

"""Importamos las librerias que necesitaremos para la practica"""
import numpy as np
import matplotlib.pyplot as plt
import math

import random
random.seed()

# Arreglos usados para mostrar la grafica
valoresParaX = np.empty([1001])
arrayDimensional = np.arange(-500, 501, 1)


"""Defininmos los parametros y dimensiones de nuestras entradas"""
NBITS = 10
NIPOP = 20
NPOP = int(random.randint(1, NIPOP))
NGOOD = int(random.randint(1, NPOP))
NBAD = NPOP - NGOOD


"""Definimos las funciones que utilizaremos para los pasos del algoritmo genetico"""

# Definciion de la funcion coste
def funcionCoste(x):
    return x * math.sin(math.sqrt(abs(x)))

def generarPoblacionInicial(NBITS, NIPOP):
    matrizIPOP = np.random.randint(2, size=(NIPOP,NBITS))
    return matrizIPOP 

"""Definicion de otras funciones herramienta que se utilizaran"""

# Funcion para graficar la funcion principal
def graficarFuncion():
    for i in range(0, 1001):
        xGraph = i - 500
    valoresParaX[i] = funcionCoste(xGraph)
    plt.plot(arrayDimensional, valoresParaX)
    plt.show()
    
    
graficarFuncion()
print(generarPoblacionInicial(NBITS, NIPOP))