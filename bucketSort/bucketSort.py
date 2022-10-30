from time import perf_counter
import matplotlib.pyplot as plt
import numpy as np

def bucketSort(input_list):
    max_value = max(input_list)
    size = max_value/len(input_list)

    buckets_list= []
    for x in range(len(input_list)):
        buckets_list.append([]) 

    for i in range(len(input_list)):
        j = int (input_list[i] / size)
        if j != len (input_list):
            buckets_list[j].append(input_list[i])
        else:
            buckets_list[len(input_list) - 1].append(input_list[i])

    for z in range(len(input_list)):
        insertionSort(buckets_list[z])
            
    final_output = []
    for x in range(len (input_list)):
        final_output = final_output + buckets_list[x]
    return final_output

def insertionSort(bucket):
    for i in range (1, len (bucket)):
        var = bucket[i]
        j = i - 1
        while (j >= 0 and var < bucket[j]):
            bucket[j + 1] = bucket[j]
            j = j - 1
        bucket[j + 1] = var 

def medir_tempo():
  tempos = []
  pioresTempos = []
  tamanhos =  [10000,20000,30000,40000,50000,80000,100000]
  for tamanho in tamanhos:
    lista = np.random.randint(0,15000, tamanho)
    inicio = perf_counter()
    bucketSort(lista)
    fim = perf_counter()
    duracao = (fim - inicio)
    tempos.append(duracao)

  for tamanho in tamanhos:
    lista = np.arange(tamanho)
    pior_caso = np.flipud(lista)
    inicio = perf_counter()
    bucketSort(pior_caso)
    fim = perf_counter()
    duracao = (fim - inicio)
    pioresTempos.append(duracao)

  return pioresTempos, tamanhos, tempos

w_tempo, lenght, a_tempo = medir_tempo()    

plt.plot(lenght, a_tempo, label = 'Melhor caso')
plt.plot(lenght, w_tempo, label = 'Pior caso')
plt.legend()
plt.title('quickSort')
plt.ylabel('Tempo em Segundos')
plt.xlabel('Itens na lista')
plt.show()