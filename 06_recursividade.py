'''
O fatorial de um número n inteiro > 1 pode ser definido, recursivamente, como:
n! = n * (n-1)!

Já o fatorial de n = 1 é definido como 1! = 1 e 0! = 1

'''

# Implementação ITERATIVA de um fatorial
def fatorial_iter(n):
    resultado = 1

    # range coemça e, m e vai descendo até o 1
    for i in range(n, 1, -1):
        resultado *= i
    return resultado

# Implementação RECURSIVA de um fatorial:
def fatorial_rec(n):
    if n == 1 or n == 0:
        return 1 # Condição de saída, pois é o ponto em que não chama a função

    elif n > 1:
        return n * fatorial_rec(n-1) # RECURSIVIDADE = CHAMAR A FUNÇÃO DENTRO DELA MESMA (PILHA DE CHAMADAS -> ESTRUTURA DE PILHAS = STACK OVERFLOW)

    else: # Números negativos
        return None # Condição de saída

# Função de fatorial recursivo sem condição de saída, para provocar um "Stack Overflow"
def fatorial_overflow(n):
    return n * fatorial_overflow(n-1)

#print(f'6! é igual a {fatorial_overflow(6)}')

##########################################################3

print(f'6! é igual a {fatorial_iter(6)}')

print(f'6! é igual a {fatorial_rec(6)}')

