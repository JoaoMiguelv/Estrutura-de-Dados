"""
    1) Identifique o algoritmo abaixo.
        Merge sort

    2) Faça o mapeamento das variáveis (registre em comentário o propósito de cada uma delas).
        a = nome da função (usada para definir a função)
        b = lista (vetor passado com os valores)
        c = meio (encontrar valor que está no meio exato na lista)
        d = sublista esquerda (cópia da primeira metade do vetor)
        e = sublista direita (cópia da segunda metade do vetor)
        f = posição esquerda (posição inicial do vetor da esquerda)
        g = posição direita (posição inicial do vetor da direita)
        h = vetor (definindo vetor para junção posteriormente)
        i = sobra (vetor criado para sobra ao realizar junção no "while")

    3) Há um erro no algoritmo. Identifique-o, descreva-o e corrija-o.
        Não foi passado o "return" ao final da função.
        
"""

def a(b):

    if len(b) <= 1: return b
    c = len(b) // 2

    d = b[:c] # sublista esquerda
    e = b[c:] # sublista direita
    d = a(d)
    e = a(e)
    f = g = 0 
    h = []

    while f < len(d) and g < len(e):
        if d[f] < e[g]:
            h.append(d[f])
            f += 1
        else:
            h.append(e[g])
            g += 1
    i = []
    if f < g:
        i = d[f:]
    else: 
        i = e[g:]

    return h + i

b = [7, 4, 2, 9, 0, 6, 5, 3, 1, 8]

resultado = a(b)
print(resultado)