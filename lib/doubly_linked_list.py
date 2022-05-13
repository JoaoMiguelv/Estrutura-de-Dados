'''
    Classe que representa uma unidade de informação na lista duplamente encadeada.
'''

from numpy import insert


class Node:

    ''' Método construtor '''
    def __init__(self, data):
        self.prev = None    # ponteiro para nodo anterior
        self.data = data    # Dado do usuário
        self.next = None    # ponteiro para nodo seguinte

######################################################################

'''
    ESTRUTURA DE DADOS LISTA DUPLAMENTE ENCADEADA
    Trata-se de uma lista linear, em que seus elementos (nodos)
    não estão adjacentes fisicamente uns dos outros, mas ligados
    logicamente por meio de ponteiros que indicam o anterior e
    o próximo nodo da sequência. Não tem restrição de acessos - 
    inserções, exclusões e consultas podem ser realizadas em
    qualquer posição da lista
'''

class DoublyLinkedList:

    ''' 'Método construtor '''
    def __init__(self):
        self.__head = None # Aponta para o primeiro nodo da lista
        self.__tail = None # Aponta para o último nodo da lista
        self.__count = 0    # Mantém o número de nodos da lista

    '''
        Propriedade que retorna a quantidade de itens da lista
    '''
    @property
    def count(self):
        return self.__count
    
    '''
        Propriedade que retorna se a lista está ou não vazia 
    '''
    @property
    def is_empty(self):
        return self.__count == 0

    '''
        Método que insere um valor na posição especificada
    '''
    def insert(self, pos, val):
        # Criamos um nodo que contém a informação do usuário e também
        # os ponteiros prev e next apontando para o None
        inserted = Node(val)

        # 1° Caso: Lista vazia e este é o primeiro nodo a ser inserido
        if self.is_empty:
            self.__head = inserted
            self.__tail = inserted
        
        # 2° Caso: Inserção na posição inicial (posição)
        elif pos == 0:
            inserted.next = self.__head
            self.__head.prev = inserted
            self.__head = inserted

        # 3° Caso: Inserção na posição final (qualquer posição >= count)
        elif pos >= self.count:
            inserted.prev = self.__tail
            self.__tail.next = inserted
            self.__tail = inserted

        # 4° Caso: Inserção na posição intermediária (entre os nodos)
        elif:
            # Encontrar o nodo anterior à posição de inserção

        
        # Incrementa a contagem de itens
        self.__count += 1
    
    '''
       Função privada que encontra o nodo da posição especificada 
    '''
