'''
    Classe que implementa a estrutura de dados pilha
'''

class Stack:
    '''Método construtor'''
    def __init__(self):
        self.__data = [] # Inicializa uma lista vazia

    '''
        MÉTODO PARA INSERÇÃO
        O nome do método de inserção em pilhas é padronizado: push()
    '''
    def push(self, val):
        # Insere val no final (topo) da pilha
        self.__data.append(val)


    '''MÉTODO PARA REMOÇÃO
    O nome também é padronizado
    '''
    def pop(self):
        
        if self.is_empty: # Tentativa de retirada de pilha vazia
            # Gera um erro
            raise Exception('ERRO: impossível retirar de uma pilha vazia')

        # A pilha não estando vazia, a retirada pode ser feita
        return self.__data.pop()

    '''
        MÉTODO QUE CONSULTA O VALOR NO TOPO DA PILHA SEM RETIRÁ-LO
        Nome padronizado: peek()
    '''
    def peek(self):
        if self.is_empty:
            raise Exception('ERRO: impossível consultar o topo de uma pilha vazia')
        
        # Retorna o último elemento da lista
        return self.__data[-1] # mesma coisa que: return self.__data[len(self.__data)-1]

    '''
        MÉTODO QUE PERMITE IMPRIMIR A PILHA:
        Método especial do Python: __str__
    '''
    def __str__(self):
        return str(self.__data)

    '''
        Propriedade somente-leitura que informa se a pilha está vazia (True) ou não (False)
    '''
    @property # transforma função em atributo -> Não precisa passar parâmetro no ()
    def is_empty(self):
        return len(self.__data) == 0