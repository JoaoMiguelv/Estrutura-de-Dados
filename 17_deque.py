from lib.deque import Deque

deque = Deque()

# Inserção de pessoas de prioridade normal
deque.insert_back('Deusdete')
deque.insert_back('Glaudemir')
deque.insert_back('Ivanilson')
deque.insert_back('Robledo')
deque.insert_back('Otaviano')

# imprime o deque
print(deque)

# inserção de uma pessoa prioritária
deque.insert_front('Berenice')

# imprime o deque
print(deque)

# remoção no final (desistência)
desistente = deque.remove_back()
print('Desistente: ',desistente)

# imprime o deque
print(deque)

# outra inserção prioritária
deque.insert_front('Laudeniza')

# imprime o deque
print(deque)

# remoção do início da fila
atendido = deque.remove_front()
print('Atendido: ', atendido)

# imprime o deque
print(deque)