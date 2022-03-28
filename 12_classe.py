# Class is a estructure that represents jointly (conjuntamente) datas and algoritms. A class is like a "cake form", who can create differents "cakes" (objects), varying the "ingredients" (datas) and the "how to do"

# (Algoritms). Although (apesar) that varying, the objects cretes from the class always have the format determinated por the form

from math import pi

class FormaGeometrica:

    # Uma classe pode ter, dentro de si, tanto dados quanto funções (estas representam os algoritmos).
    # Uma função especial denominada __init__, é chamada sempre que um novo objeto é criado a partir da classe, sendo conhecido como CONSTRUTOR.
    # Quando estão dentro de uma classe, as funções passam a ser chamados de MÉTODOS, e *sempre* têm self (que retornam para si mesmo) como primeiro parâmetro, representando o próprio objeto.

    def __init__(self, base, altura, tipo):
        # Recebemos os parametros no construtor e armazenamos dentro do objeto que está sendo criado
        self.base = base
        self.altura = altura
        self.tipo = tipo

########################################################

# CRIANDO OBJETOS A PARTIR DA CLASSE
forma1 = FormaGeometrica(12, 7, 'R') # Isso chama __init__()
forma2 = FormaGeometrica(7.5, 8.2, 'T')

print(f"forma1: base {forma1.base}, altura {forma1.altura}, tipo {forma1.tipo}")
print(f"forma2: base {forma2.base}, altura {forma2.altura}, tipo {forma2.tipo}")
