"""
    1) Identifique o algoritmo abaixo.
        Busca sequencial

    2) Faça o mapeamento das variáveis (registre em comentário o propósito de cada uma delas).
        a = nome da função (usada para definir a função)
        b = valor (valor a ser procurado dentro da lista)
        c = lista (vetor passado com os valores)

    3) Há um erro no algoritmo. Identifique-o, descreva-o e corrija-o.
        Dentro do "for", foi passado o "c in range". No caso, deveria ter sido passado um valor que vai variar a cada vez que o for rodar (para corrigir, chamarei de "i").
        Além disso, outro erro foi ao definir o "len(b)", que está medindo o tamanho do valor e não da lista. Para corrigir, basta trocar o "b" por "c".
        Agora dentro do for há mais erros: foi passado o valor no lugar da lista ao validar com o "if" e ao definir a posição, foi passado o valor do vetor inteiro. Vamos corrigir alterando o "b" para "c" e dentro dos "[]" colocaremos "i".
        Após isso, também foi trocado após o "==" os valores de "valor" pelo de "lista" e o retorno deve ser de "i".
        OBS: poderia ter sido alterado a ordem dos valores ao chamar a função, porém preferi deixar no padrão conforme passado em aula

"""

def a(b, c):
    for i in range(len(c)):
        if c[i] == b: return i
    return -1

c = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60]

print(f'Posição de 18: {a(18, c)}')