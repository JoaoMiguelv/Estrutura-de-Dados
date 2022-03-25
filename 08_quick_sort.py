'''
 ALGORITIMO DE ORDENAÇÂOI QUICK SORT

 Escolhe um dos elementos da lista para ser pivo (na nossa implementação, o ultimo elemento) e, na primeira passada, divide a lista, a partir da posição final da lista em uma sublista a esquerda contendo apenas valores menores que o pivo, e outra sublista a direita, que contem apenas valores maiores que o pivo

 Em seguida, recursivamente, repete o processo em cada uma das sublista até que toda lista esteja ordenada 
'''
from data.nomes_desord import nomes
from time import time
import tracemalloc

passadas = comps = trocas = 0

def quick_sort (lista, ini = 0, fim = None):
    
    #se fim for none, o colocamos na posição do ultimo elemento da lista
    if fim is None: fim = len(lista) - 1

    # Para que o algoritimo de ordenação trabalhe, é necessario que haja pelo menos dois elementos na faixa delimitada por ini e fim
    if fim <= ini: return #sai da função sem fazer nada

    global passadas,comps,trocas
    passadas += 1
    #inicialização das variaveis de controle
    pivot = fim
    div = ini -1

    #percorre a lista da posição ini até a posição fim -1
    for i in range(ini, fim):
    #compara os elementos das posições i e pivot
        comps += 1
        if lista[i] < lista[pivot]:
            div += 1 # incrementa a posição div
            # se i e div nao forem a mesma posição, eles troca de posição
            if div != i:
                lista[i], lista[div] = lista[div], lista[i]
                trocas += 1
    #Depois que o loop acaba, o divisor sofre um ultimo incremento 
    div += 1

    #Os elementos da posição de div e da posição de pivot trocam de lugar entre si se:
    # 1) as posições div e pivot forem diferentes entre si
    # 2) lista[pivot] for menor que lista[div]
    comps += 1
    if div != pivot and lista[pivot] < lista[div]:
        lista[pivot], lista[div] =  lista[div], lista[pivot]
        trocas += 1


    # Chamada recursiva a funcção para ordenar a sublista a esquerda da posição div
    quick_sort(lista, ini, div-1)

    # Chamada recursiva a funcção para ordenar a sublista a direita da posição div
    quick_sort(lista, div+1, fim)

#----------------------------------------------------------------------------------------------------------------------#

nums = [7,4,2,9,0,6,8,3,1,5]
#nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
#nums = [0,1,2,3,4,5,6,7,8,9]

quick_sort(nums)

print(f'Passadas: {passadas}, comparações: {comps}, trocas: {trocas}')

hora_ini = time()
tracemalloc.start() # Inicia o monitoramento da memória

nomes_ord = quick_sort(nomes)

# Captura as estatísticas do uso da memória
mem_atual, mem_pico = tracemalloc.get_traced_memory() # Função que retorna dois valors (se deixar somente 1 variavel, irá ignorar a segunda resposta da função)
hora_fim = time()

print(nomes[:100]) # Imprime só os 100 primeiros nomes

print(f'Tempo gasto para ordenar: {(hora_fim - hora_ini)*1000}ms')
print(f'Pico de memória: {mem_pico / 1024 / 1024} MB')
print(f'Passadas: {passadas}, comparações: {comps}, trocas: {trocas}')