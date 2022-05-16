from lib.doubly_linked_list import DoublyLinkedList

lista = DoublyLinkedList()
print(lista)

# Inserção em lista vazia: a posição será ignorada
lista.insert(5, 'Epaminondas')
print(lista)

#  Inserção no início da lista
lista.insert_head('Felisberto') # Equivale a: lista.insert(0, 'Felisberto')
print(lista)

# Inserção no final da lista
lista.insert_tail('Jerusa') # Equivale a: lista.insert(lista.count, 'Jerusa')
print(lista)

# Inserção em posição intermediária
lista.insert(2, 'Laudicéia')
print(lista)
