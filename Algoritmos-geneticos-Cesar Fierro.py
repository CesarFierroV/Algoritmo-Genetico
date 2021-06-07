# -*- coding: utf-8 -*-
"""
Created on Sat May 15 14:58:09 2021

@author: Cesar Fierro
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

"""Definimos las funciones que utilizaremos para los pasos del algoritmo genetico"""

# Definciion de la funcion coste
def funcionCoste(x):
    return x * math.sin(math.sqrt(abs(x)))

# Funcion que genera la poblacion inicial tomando como parametros los valores de NBITS y NIPOP
# Devuelve una matriz binaria de NIPOP x NBITS, llena con 0'S y 1's aleatoriamente
def generarPoblacionInicial(NBITS, NIPOP):
    matrizIPOP = np.random.randint(2, size=(NIPOP,NBITS))
    return matrizIPOP 

# Funcion mating pool para seleccionar los mejores cromosomas
def matingPool(matrizIPOP, NPOP, NGOOD):
    # Iniciar iteracion
    # Generamos su valor en decimal
    matrizIPOPDecimal = convertirMatrizBinariaAListaEntera(matrizIPOP)
    # Generamos los costos para cada individuo
    listaDeCostos = obtenerListaCostoDeX(matrizIPOPDecimal)
    # Ordenamos los costos de menor a mayor, mas adelante utilizaremos esto para ordenar la matriz
    listaDeCostosOrdenada = ordenarCostesDeMenorAMayor(obtenerListaCostoDeX(matrizIPOPDecimal))
    
    """Imprimimos la informacion de la matriz generada aleatoriamente desordenada"""
    print("Valores Iniciales")
    print("Matriz IPOP", "\t\t ", "Valores en Decimal", "Valores de coste")
    for i in matrizIPOP:
        print(i, "\t", convertirListaBinariaAEntero(i), "\t\t\t", funcionCoste(convertirListaBinariaAEntero(i)))
    print("\n")
    
    """Ordenamos la matriz de menor a mayo de acuerdo a los costos"""
    matrizIPOPordenada = listasOrdenadas(matrizIPOP, listaDeCostos, listaDeCostosOrdenada)
    
    """Imprimimos la informacion de la matriz Ordenada"""
    print("Valores ordenados de menor a mayor de acuerdo al valor de coste")
    print("Matriz IPOP", "\t\t ", "Valores en Decimal", "Valores de coste")
    for i in matrizIPOPordenada:
        print(i, "\t", convertirListaBinariaAEntero(i), "\t\t\t", funcionCoste(convertirListaBinariaAEntero(i)))
    print("\n")
    
    """Imprimimos NPOP y obtenemos la matriz NPOP"""
    print("NPOP: ", NPOP)
    matrizNPOP = matrizIPOPordenada[0:NPOP]
    print(matrizNPOP)
    print("\n")
    
    """Imprimimos NGOOD y obtenemos la matriz NGOOD"""
    print("NGOOD: ", NGOOD)
    matrizNGOOD = matrizIPOPordenada[0:NGOOD]
    
    print(matrizNGOOD)
    print("\n")
    return matrizNGOOD
    
def seleccionDeParejasYCruce(matrizNGOOD):
    nuevaMatrizIPOP = np.copy(matrizNGOOD)
    # Primero calculamos el punto de cruce
    puntoDeCruce = np.random.randint(1, len(matrizNGOOD[0]))
    print("Cruce sencillo")
    print("Punto de Cruce:", puntoDeCruce)
    
    # Si tenemos un numero par, se forman las parejas y pasan sus descendientes
    # si es un numero impar el ultimo elemento pasa directo
    if len(matrizNGOOD) % 2 == 0:
        par = 0
    else:
        par = 1
    
    #Cruzamos los padres y obtenemos descendientes de los cuales formamos una matriz de una nueva poblacion
    for i in range(0, len(matrizNGOOD) - par, 2):
        nuevaMatrizIPOP[i][:puntoDeCruce] = matrizNGOOD[i][:puntoDeCruce]
        nuevaMatrizIPOP[i][puntoDeCruce:] = matrizNGOOD[i + 1][puntoDeCruce:]
        
        nuevaMatrizIPOP[i + 1][:puntoDeCruce] = matrizNGOOD[i + 1][:puntoDeCruce]
        nuevaMatrizIPOP[i + 1][puntoDeCruce:] = matrizNGOOD[i][puntoDeCruce:]
        
    print("Nueva Poblacion")
    print(nuevaMatrizIPOP)
    print("\n")
    return nuevaMatrizIPOP
    
def mutacion():
    pass

# Funcion que compara el elemento mas apto con el modelo y devuelve si se llego a la convergencia
def convergencia(poblacion, modelo):
    for elemento in poblacion:
        if (elemento == modelo).all():
            return True
    return False

"""Definicion de otras funciones herramienta que se utilizaran"""

# Funcion para graficar la funcion principal
def graficarFuncion():
    
    for i in range(0, 1001):
        xGraph = i - 500
        valoresParaX[i] = funcionCoste(xGraph)
    plt.plot(arrayDimensional, valoresParaX)
    plt.show()

# Funcion que grafica la funcion fitness y el minimo encontrado
def graficarMinimo(pointX, pointY):
    for i in range(0, 1001):
        xGraph = i - 500
        valoresParaX[i] = funcionCoste(xGraph)
    plt.plot(arrayDimensional, valoresParaX)
    plt.scatter(pointX, pointY)
    plt.show()


# Funcion que convierte una matriz Binaria en una lista decimal, tomando en cuenta el signo
def convertirMatrizBinariaAListaEntera(matrizIPOP):
    listaCromosomasInt = []
    for listaBinaria in matrizIPOP:
        if listaBinaria[0] == 0:
            signo = "-"
        else:
            signo = ""
        strNumeroEntero = ""
        for i in range(1,10):
            strNumeroEntero += str(listaBinaria[i])
        listaCromosomasInt.append(int(signo + strNumeroEntero, 2))
    return listaCromosomasInt

# Funcion que convierte una lista binaria a un numero decimal
def convertirListaBinariaAEntero(listaBinaria):
    if listaBinaria[0] == 0:
        signo = "-"
    else:
        signo = ""
    strNumeroEntero = ""
    for i in range(1,10):
        strNumeroEntero += str(listaBinaria[i])
    return int(signo + strNumeroEntero, 2)

# Funcion que ordena los costos de menos a mayor
def ordenarCostesDeMenorAMayor(listaCromosomasAOrdenar):
    listaCromosomasAOrdenar.sort()
    return listaCromosomasAOrdenar

# Funcion que toma la matrizIPOP binaria original y la ordena de acuerdo a los costos
def listasOrdenadas(matrizBinaria, listaCostos, listaDeCostosOrdenada):
    nuevaMatrizBinaria = np.copy(matrizBinaria)
    for i in range(0, len(listaDeCostosOrdenada)):
        index = listaCostos.index(listaDeCostosOrdenada[i])
        nuevaMatrizBinaria[i] = matrizBinaria[index]
    return nuevaMatrizBinaria


# Funcion que toma la lista de decimales y obtiene el costo para cada elemento
def obtenerListaCostoDeX(listaCromosomasInt):
    listaCostosX = []
    for x in listaCromosomasInt:
        listaCostosX.append(funcionCoste(x))
    return listaCostosX



def main():
    graficarFuncion()
    
    """Defininmos los parametros y dimensiones de nuestras entradas"""
    NBITS = 10
    NIPOP = 20
    NPOP = int(random.randint(2, NIPOP))
    NGOOD = int(random.randint(2, NPOP))
    NBAD = NPOP - NGOOD
    MODELO = np.array([0, 1, 1, 0, 1, 0, 0, 1, 0, 1]) # =-421
    
    # Imprimimos el modelo
    print("Modelo:")
    print(MODELO)
    print("\n")
    
    # Generamos la poblacion inicial llamando a la funcion y guardando el valor de retorno en la
    # variable "matrizIPOP"
    matrizIPOP = generarPoblacionInicial(NBITS, NIPOP)
    print("Matriz generada aleatoriamente")
    print(matrizIPOP)
    print("\n")

    for i in range(0, 2):
        """Comienza mating pool"""
        # Ordenamos los elementos de menor a mayor, imprime los valores iniciales desordenados,
        # los valores ordenados de acuerdo al coste y devuelve una matriz con los valores NGOOD
        matrizNGOOD = matingPool(matrizIPOP, NPOP, NGOOD)
    
    
        """Comienza Seleccion de pareja y Cruce"""
        nuevaPoblacion = seleccionDeParejasYCruce(matrizNGOOD)
        
        """No se realiza mutacion"""
        #mutacion()
    
        """Revisamos si se cumple la convergencia"""
        if convergencia(nuevaPoblacion, MODELO):
            print("convergencia alcanzada, mostrando minimo")
            break
        else:
            print("Convergencia no alcanzada")
            """Reescribimos el valor de NIPOP, NPOP y NGOOD"""
            NIPOP = len(nuevaPoblacion)
            NPOP = int(random.randint(2, NIPOP))
            NGOOD = int(random.randint(2, NPOP))
        print("\n")
        matrizIPOP = np.copy(nuevaPoblacion)
        
    print("Minimo encontrado")
    print(nuevaPoblacion[0])
    print(convertirListaBinariaAEntero(nuevaPoblacion[0]))
    print("Coste:", funcionCoste(convertirListaBinariaAEntero(nuevaPoblacion[0])))
    graficarMinimo(convertirListaBinariaAEntero(nuevaPoblacion[0]), funcionCoste(convertirListaBinariaAEntero(nuevaPoblacion[0])))
        
if __name__=="__main__":
    main()
