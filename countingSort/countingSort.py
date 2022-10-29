from time import perf_counter
import matplotlib.pyplot as plt
import numpy as np

def countingSort(lista):
    
    count = [0]*(max(lista)+1)
    res = [0]*len(lista)
    for num in  lista:
        count[num] = count[num]+1
    for i in range(1,len(count)):
        count[i] = count[i-1]+count[i]
    for num in lista:
        res[count[num]-1] = num
        count[num] = count[num]-1

def medir_tempo():
  tempos = []
  pioresTempos = []
  tamanhos =   [100000,200000,300000,400000,500000,800000,1000000]
  for tamanho in tamanhos:
    lista = np.random.randint(0,1000000, tamanho)
    inicio = perf_counter()
    countingSort(lista)
    fim = perf_counter()
    duracao = (fim - inicio)
    tempos.append(duracao)

  return tamanhos, tempos

lenght, a_tempo = medir_tempo()

plt.plot(lenght, a_tempo, label = 'tempo de ordenação')
plt.legend()
plt.title('CoutingSort')
plt.ylabel('Tempo em Segundos')
plt.xlabel('Itens na lista')
plt.show()