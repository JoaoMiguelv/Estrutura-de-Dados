"""
    1) Identifique o algoritmo abaixo.
        Selection Sort
    2) Faça o mapeamento das variáveis (registre em comentário o propósito de cada uma delas).
    a = nome da função do selection sort (usada para definir a função)
    b = lista (vetor passado com os valores)
    c = nome da função que encontra a menor posição
    d = posição inicial (parâmetro para definir a posição inicial da sublista)
    e = posição final (parâmetro para definir a posição final da sublista)
    f = posição resposta
    g = posicão (definido para ser alterado a cada loop que o for dá)
    h = pos_sel (posição de seleção para realizar a validação)
    i = posição menor (menor valor encontrado na região de busca)

    3) Há um erro no algoritmo. Identifique-o, descreva-o e corrija-o.
        O erro se encontra no "return", que ao invés de retornar a posição resposta, estava retorno a posicão. Basta trocar "g" por "f"
"""

def a(b):
    def c(d, e):
        f = d
        for g in range(d + 1, e + 1):
            if b[g] < b[f]:
                f = g
        return f
    for h in range(len(b) - 1):
        i = c(h + 1, len(b) - 1)
        if b[i] < b[h]:
            b[i], b[h] = b[h], b[i]

b = [9, 0, 1, 2, 3, 4, 5, 6, 7, 8]
a(b)
print(b)