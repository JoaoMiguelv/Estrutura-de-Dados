# Class is a estructure that represents jointly (conjuntamente) datas and algoritms. A class is like a "cake form", who can create differents "cakes" (objects), varying the "ingredients" (datas) and the "how to do"

# (Algoritms). Although (apesar) that varying, the objects cretes from the class always have the format determinated por the form

from math import pi
from msilib.schema import Property

class FormaGeometrica:

    # Uma classe pode ter, dentro de si, tanto dados quanto funções (estas representam os algoritmos).
    # Uma função especial denominada __init__, é chamada sempre que um novo objeto é criado a partir da classe, sendo conhecido como CONSTRUTOR.
    # Quando estão dentro de uma classe, as funções passam a ser chamados de MÉTODOS, e *sempre* têm self (que retornam para si mesmo) como primeiro parâmetro, representando o próprio objeto.

    def __init__(self, base, altura, tipo):
        # Recebemos os parametros no construtor e armazenamos dentro do objeto que está sendo criado
        self.base = base
        self.altura = altura
        self.tipo = tipo

        ''' SETTER E GETTER
        
        self.set_base(base) # ATRIBUTO PRIVADO. Só podem ser lidos/acessados dentro da classe
        self.set_altura(altura)
        self.set_tipo(tipo)

    
    # Métodos setter (ajustam o valor de atributos __privados)
    
    def set_base(self, valor):
        if type(valor) not in [int, float] or valor <= 0:
            raise Exception('* A base deve ser númerica e maior que zero')
        self.__base = valor

    def set_altura(self, valor):
        if type(valor) not in [int, float] or valor <= 0:
             raise Exception('* A altura deve ser númerica e maior que zero')
        self.__altura = valor

    def set_tipo(self, valor):
        if valor not in ['R', 'T', 'E']:
            raise Exception("* O tipo deve ser 'R', 'T' ou 'E'.")
        self.__tipo = valor

    # Métodos getter (retornam o valor de atributos __privados)
    def get_base(self):
        return self.__base
    
    def get_altura(self):
        return self.__altura
    
    def get_tipo(self):
        return self.__tipo
    '''
    # PROPRIEDADES

    @property # Annotation (ANOTAÇÃO COMO PROPRIEDADE)
    def base(self): # getter "disfarçado"
        return self.__base
    @base.setter
    def base(self, valor):  # setter disfarçado
        if type(valor) not in [int, float] or valor <= 0:
            raise Exception('* A base deve ser númerica e maior que zero')
        self.__base = valor


    @property
    def altura(self):
        return self.__altura
    @altura.setter
    def altura(self, valor):
        if type(valor) not in [int, float] or valor <= 0:
             raise Exception('* A altura deve ser númerica e maior que zero')
        self.__altura = valor


    @property
    def tipo(self):
        return self.__tipo
    @tipo.setter
    def tipo(self, valor):
        if valor not in ['R', 'T', 'E']:
            raise Exception("* O tipo deve ser 'R', 'T' ou 'E'.")
        self.__tipo = valor
########################################################
    # MÉTODO PARA CÁLCULO DA ÁREA DA FORMA GEOMÉTRICA
    @property # Redefinindo como propriedade somente-leitura (só tem getter)
    def area(self):
        from math import pi
        if(self.tipo == 'R'): #RETÂNGULO
            return self.base * self.altura
        elif(self.tipo == 'T'): #TRIÂNGULO
            return self.base * self.altura / 2
        else:   #ELIPSE
            return(self.base/2)*(self.altura/2)*pi

########################################################
# CRIANDO OBJETOS A PARTIR DA CLASSE
forma1 = FormaGeometrica(12, 7, 'R') # Isso chama __init__()
forma2 = FormaGeometrica(7.5, 8.2, 'T')

# forma1.set_base("farinha") # Alterando um atributo privado por meio de uma função pública

# print(f"forma1: base {forma1.get_base()}, altura {forma1.get_altura()}, tipo {forma1.get_tipo()}")
# print(f"forma2: base {forma2.get_base()}, altura {forma2.get_altura()}, tipo {forma2.get_tipo()}")

#forma2.altura = "dois palmos"

# print(f"forma1: base {forma1.base}, altura {forma1.altura}, tipo {forma1.tipo}")
# print(f"forma2: base {forma2.base}, altura {forma2.altura}, tipo {forma2.tipo}")

print(f"forma1: base {forma1.base}, altura {forma1.altura}, tipo {forma1.tipo}, área {forma1.area}")
print(f"forma2: base {forma2.base}, altura {forma2.altura}, tipo {forma2.tipo}, área {forma1.area}")