# FUNÇÃO CALCULAR IMC
from numpy import append, insert


def Calcular_Imc():

    peso = float(input('Peso: '))
    altura = float(input('Altura: '))

    peso_format = "{:0.2f}".format(peso)
    altura_format = "{:0.2f}".format(altura)
    
    print('Peso:',peso_format)
    print('Altura:',altura_format)

    imc = peso / (altura**2)
    imc_format = "{:0.2f}".format(imc)

    print('IMC:',imc_format)

# FUNÇÃO ÁREA FORMA GEOMÉTRICA
def calcular_area(base, altura, forma):

    if forma == 'R': #Retângulo
        return base*altura

    elif forma == 'T': #Triângulo
        return base*altura/2
    
    elif forma == 'E': #Elipse
        return (base/2) * (altura/2) * 3.1416 #PI ou usar o FROM MATH IMPORT PI
    
    else:
        return None

# EXEMPLOS DE CHAMADA DA FUNÇÃO:

print(f'Retângulo 15x25: {calcular_area(15, 25, "R")}')

print(f'Triângulo 12x16: {calcular_area(12, 16, "T")}')

print(f'Elipse 10x20: {calcular_area(10, 20, "E")}')




