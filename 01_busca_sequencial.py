# BUSCA SEQUENCIAL
#
# Procura por um valor na lista, partindo do primeiro elemento até o último. Retorna:
# A) A posição do elemento, caso ele exista
# B) -1, se o elemento NÃO existir

nums = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60]

''' FUNÇÃO QUE IMPLEMENTE A BUSCA SEQUENCIAL
Se existir: n° de comparações = posição + 1
Se não existir: n° de comparações = n (qte de itens da lista)
'''

def busca_sequencial(val, lista):

    for pos in range(len(lista)):
        # Se encontra coincidência, retona a posição
        if lista[pos] == val: return pos

    return -1 #Nda encontrado

print(f'Posição de 27: {busca_sequencial(27, nums)}')
print(f'Posição de 27: {busca_sequencial(40, nums)}')

