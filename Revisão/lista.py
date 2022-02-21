
def listas_vetores():
    valores = [1, 2, 3, 4, 8, 9, 10, 11, 58, 96, 36, 98, 45]

    valores.append(5) #Incluir no final da lista 
    valores.insert(0, 6) #Definir a posição do novo elemento na lista (POSIÇÃO: 0, ELEMENTO: 6)
    print(valores)

    print('Número de elementos na lista:', len(valores))

    ultimo = valores.pop() #Remove o ÚLTIMO ELEMENTO DA LISTA
    print(f'{ultimo} era o último elemento')
    print(f'Lista sem o último elemento: {valores}')

    del valores[1] #Remove o elemento na posição 1
    print(f'Lista sem o elemento DE POSIÇÃO 1: {valores}')

    valores.remove(2) #Remove o valor 2 EM ESPECÍFICO
    print(f'Lista sem o elemento 2 : {valores}')

    sublista = valores[2:7] #Criando uma sublista ("Fatiando a lista") vai da POSIÇÃO 2 A POSIÇÃO 6 (EXCLUI O 7)
    print(f'Sublista: {sublista}')

    print('Sublista da posição inical até a posição 8:', valores[:8]) #Vai de 0 até 8

listas_vetores()