'''
ALGRITMO DE ORDENAÇÃO SELECTION

Isola (seleciona) o primeiro elemento da lista e, em seguida, encontra o menor valor nos restante da isa. Se o valor encontrado for menor que o valor selecinado, efetua a troca. Em seguida, isola o segundo número da lista, buscando pelo menor valor das posições subsequentes. Faz a troca entre os dois valores, se necessário. Continua o processo, até isolar o penúltimo elemento da lista

'''
from data.nomes_desord import nomes
from time import time

passadas = comps = trocas = 0

def selection_sort(lista):

    global passadas, comps, trocas
    passadas = comps = trocas = 0

    # Subgunção que encontra o menor valor na sublista delimitada por pos_ini e pos_fim
    def encontrar_pos_menor(pos_ini, pos_fim):
        global comps
        
        pos_resposta = pos_ini
        #Loop da segunda até a última posição
        for pos in range(pos_ini + 1, pos_fim +1):
            comps += 1
            if lista[pos] < lista[pos_resposta]:
                pos_resposta = pos

        return pos_resposta

    # Loop que vai da primeira até a PENÚLTIMA posição
    for pos_sel in range(len(lista)-1):
        passadas += 1

        #pos_menor = menor número entre pos_sel +1 e len(lista)-1 (REGIÃO DE BUSCA)
        #Encontra o menor valor na faixa entre o número seguinte a pos_sel e o fim da lista
        pos_menor = encontrar_pos_menor(pos_sel+1, len(lista)-1)

        comps += 1
        # Compara se o menor valor encontrado é ainda menor que o valor selecionado
        if lista[pos_menor] < lista[pos_sel]:
            trocas += 1
            #Efetua a troca
            lista[pos_menor], lista[pos_sel] = lista[pos_sel], lista[pos_menor]


##################################################################################


#nums = [7, 4, 2, 9, 0, 6, 5, 3, 1, 8]
#nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#nums =[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
nums = [9, 0, 1, 2, 3, 4, 5, 6, 7, 8] # PIOR CASO PARA O SELECTION SORT
selection_sort(nums)
print(nums)
print(f'Passadas: {passadas}, Comparações: {comps}, Trocas: {trocas}')