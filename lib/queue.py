'''
    ESTRUTURA DE DADOS FILA (QUEUE)
    É uma estrutura de dados linear em que tanto a operação de inserção (ENQUEUE) acontece no final (ou cauda)
    e a operação de remoção (DEQUEUE) ocorre no início (ou cabeça).

    Como consequência, o funcionamento da fila pode ser definido como FIFO (Fist In, First Out):
    o primeiro a entrar é o primeiro a sair.
'''

class Queue:

    '''Método construtor'''
    def __init__(self):
        #Inicializa uma lista vazia
        self.__data = []

    '''
        MÉTODO PARA INSERÇÃO
        Nome padronizado: enqueue()
    '''
    def enqueue(self, val):
        self.__data.append(val)

    '''
        MÉTODO PARA REMOÇÃO
        Nome padronizado: dequeue()
    '''
    def dequeue(self):
        if self.is_empty:
            raise Exception('Erro: impossível remover de uma fila vazia')

        # Remove o primeiro elemento da fila
        return self.__data.pop(0)
    
    '''
        MÉTODO QUE CONSULTA O VALOR NA CABEÇA DA FILA SEM RETIRÁ-LO
        Nome padronizado: peek()
    '''
    def peek(self):
        if self.is_empty:
            raise Exception('ERRO: impossível consultar a cabeça de uma pilha vazia')

        # Retorna o último elemento da lista
        return self.__data[0]


    '''
        MÉTODO QUE PERMITE IMPRIMIR A FILA:
        Método especial do Python: __str__
    '''
    def __str__(self):
        return str(self.__data)



    '''
        Propriedade somente-leitura que informa se a filha está vazia (True) ou não (False)
    '''
    @property # transforma função em atributo -> Não precisa passar parâmetro no ()
    def is_empty(self):
        return len(self.__data) == 0
