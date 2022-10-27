import numpy as np
import matplotlib.pyplot as plt
from random import randint
from time import perf_counter


def selection(lista):
    for i in range(0, len(lista) - 1):
        min = i
        for j in range(i + 1, len(lista)):
            if (lista[j] < lista[min]):
                min = j
        aux = lista[min]
        lista[min] = lista[i]
        lista[i] = aux
    return lista


def criarLista(length):
    lista = []
    while len(lista) < length:
        element = randint(1, 1*length)
        if element not in lista:
            lista.append(element)
    return lista


def counter():

    tempoMedio = []
    tempoMelhor = []
    tempoPior = []

    list_length = [1000, 2000, 3000, 4000, 5000, 8000, 11000, 15000]

    for i in list_length:
        casoMedio = criarLista(i)
        casoMelhor = sorted(casoMedio)
        casoPior = sorted(casoMelhor, reverse=True)

        inicio = perf_counter()
        selection(casoMedio)
        final = perf_counter()
        duracao = final - inicio
        tempoMedio.append(duracao)

        inicio = perf_counter()
        selection(casoMelhor)
        final = perf_counter()
        duracao = final - inicio
        tempoMelhor.append(duracao)

        inicio = perf_counter()
        selection(casoPior)
        final = perf_counter()
        duracao = final - inicio
        tempoPior.append(duracao)

    return tempoPior, tempoMedio, tempoMelhor, list_length


w_tempo, m_tempo, b_tempo, lenght = counter()

plt.plot(lenght, b_tempo, label='Melhor caso')
plt.plot(lenght, m_tempo, label='Caso médio')
plt.plot(lenght, w_tempo, label='Pior caso')
plt.legend()
plt.title('selection sort')
plt.ylabel('Tempo em Segundos')
plt.xlabel('Itens na lista')
plt.show()
