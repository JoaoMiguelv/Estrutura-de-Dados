'''
Um dicionário é uma estrutura de dados fornecida pela linguagem Python capaz de armazenar múltiplps valores em uma única variável,
por meio de pares de chave-valor.
'''

pessoa = {
    # "nome" é a chave
    # "Gervársio Gomes Garcia" é o valor

    "nome": "Gervársio Gomes Garcia",
    "sexo": "M",
    "idade": 69,
    "peso": 76,
    "altura": 1.77
}

# Acessando os valores armezenados no dicionário
print(f"Nome: {pessoa['nome']}")
print(f"Idade: {pessoa['idade']}")

# Calculando o IMC
imc = pessoa["peso"] / pessoa["altura"] ** 2
print(f"IMC: {imc}")

############################################################

# Formas geométricas representadas na fora de dicionário
forma1 = {
    "base": 7.5,
    "altura": 12,
    "tipo": "R" # RETÂNGULO
}

forma2 = {
    "base": 6,
    "altura": 2.5,
    "tipo": "T" # TRIÂNGULO
}

forma3 = {
    "base": 5,
    "altura": 3,
    "tipo": "E" # ELIPSE
}

forma4 ={
    "base": 10,
    "altura": 5,
    "tipo": "R" # RETÂNGULO
}

# FORMA GEOMÉTRICA COMPLETAMENTE ANÔMALA
forma5 ={
    "legume": "batata",
    "fruta": "jabuticaba",
    "tipo": "T" # TRIÂNGULO PARA DAR ERRO
}

# INSERINDO AS FORMAS EM UMA LISTA PARA PERCORRER COM FOR
lista_formas = [forma1, forma2, forma3, forma4, forma5]

# FUNÇÃO QUE CALCULA A ÁREA DE UMA FORMA DE ACORDO COM A BASE, A ALTURA E O TIPO
from math import pi

def calcular_area(forma):
    if forma["tipo"] == 'R':
        return forma["base"] * forma["altura"]

    elif forma["tipo"] == 'T':
        return forma["base"] * forma["altura"] / 2

    elif forma["tipo"] == 'E':
        return (forma["base"]/2) * (forma["altura"]/2) * pi
    
    else:   # Shape unrecognized
        raise Exception('ERRO: Geometric shape type is not recognized') # Gera um erro

# Calculating area from shapes of list
for i in range(0, len(lista_formas)):
    print('-'*30)
    print(f'Calculando área da forma{i+1}:')

    print(F"Tipo: {lista_formas[i]['tipo']}; base: {lista_formas[i]['base']}; altura: {lista_formas[i]['altura']}; ÁREA: {calcular_area(lista_formas[i])}")


