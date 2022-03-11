'''
ALGORITMO DE ORDENAÇÃO BUBBLE SORT

Percore a lista a ser ordenada em sucessivas passadas, trocando elementos adjacentes entre si quando o segundo for menor que o primeiro.
Efetua tantas passadas quanto necessárias até que, na última passada, nenhuma troca seja efetuada

ESSA VERSÃO É OTIMIZADA PARA QUE O LOOP DAS PASSADAS VÁ ENCONLHENDO À MEDIDA QUE OS ÚLTIMOS VALORES VÃO OCUPANDO SEUS DEVIDOS LUGARES
'''
from data.nomes_desord import nomes
from time import time

passadas = 0
comps = 0
trocas = 0

def bubble_sort(lista):

    #Declara o uso de variáveis globais
    global passadas, comps, trocas
    passadas = comps = trocas = 0
    limite = 1 # Controla até onde vai o oop for

    while True: # Loop eterno (Não sabemos quantas passadas serão necessárias)
        passadas += 1
        trocou = False # Controla se houve ou não trocas
        

        for pos in range(len(lista)-limite):
            # O -1 é para definir o PERCURSO da lista da PRIMEIRO até o PENÚLTIMA POSIÇÃO. Pois sempre será analisado a posição atual e a posição a frente, por isso nunca pode chegar na última posição
            comps += 1

            if lista[pos] > lista[pos+1]:
                # Troca os elementos de posição
                lista[pos], lista[pos+1] = lista[pos+1], lista[pos]
                trocou = True
                trocas += 1
        
        # Se não houve trocas, interrompe o loop de passadas
        if not trocou:
            break

        limite += 1 

#nums = [7, 4, 2, 9, 0, 6, 5, 3, 1, 8]
#nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] # MELHOR caso para o bubble sort (lista totalmente ORDENADA)
nums =[9, 8, 7, 6, 5, 4, 3, 2, 1, 0] # PIOR caso para o bubble sort (lista totalmente INVERSA)

bubble_sort(nums)
print(nums)
print(f'Passadas: {passadas}, Comparações: {comps}, Trocas: {trocas}')

# hora_ini = time()
# bubble_sort(nomes)
# hora_fim = time()

# print(f'Tempo gasto para ordenar: {(hora_fim - hora_ini)*1000}ms')
# print(nomes)
# print(f'Passadas: {passadas}, Comparações: {comps}, Trocas: {trocas}')
