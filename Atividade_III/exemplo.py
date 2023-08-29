from abc import ABC, abstractmethod
'''
Um método abstrato é um método declarado em uma classe base (ou classe mãe), mas não é implementado nessa classe. Em vez disso, as classes filhas que herdam da classe base são obrigadas a implementar esse método. 
Os métodos estáticos são definidos usando o decorador @staticmethod e não têm acesso ao estado da instância da classe. Isso significa que eles não podem acessar atributos de instância ou métodos de instância. 
Os métodos estáticos são geralmente usados para criar funções relacionadas à classe que não precisam interagir com os atributos de instância.
'''
class Nome:
    def __init__(self, nome) -> None:
        self.nome = nome
class Dono:
    def __init__(self, nome_dono) -> None:
        self.nome_dono = nome_dono

class Veiculo:
    def __init__(self, nome, nome_dono, fabricante) -> None:
        self.nome = nome
        self.nome_dono = nome_dono
        self.fabricante = fabricante
    
    @abstractmethod #Metodo abstrato
    def andando(self):
        pass
class Carro(Veiculo): #Heranca
    def __init__(self, nome, nome_dono, fabricante) -> None:
        super().__init__(nome, nome_dono, fabricante)
    
    def andando(self):
        return f'{self.nome.nome} está andando!'
    
class Moto(Veiculo):
    def __init__(self, nome, nome_dono, fabricante) -> None:
        super().__init__(nome, nome_dono, fabricante)

    def andando(self):
        return f'{self.nome.nome} está andando!'

class MathUtils:
    @staticmethod #Metodo estatico
    def add(a, b):
        return a + b
    
class ClassA:
    def method_a(self):
        print("Method from ClassA")

class ClassB:
    def method_b(self):
        print("Method from ClassB")

class ClassC(ClassA, ClassB):
    def method_c(self):
        print("Method from ClassC")

obj = ClassC() #Heranca multipla 
obj.method_a()  # Output: Method from ClassA
obj.method_b()  # Output: Method from ClassB
obj.method_c()  # Output: Method from ClassC


def andar(veiculo):
    return veiculo.andando()

nome1 = Nome('Ford Ka') #Composicao eh uma relacao com mais dependencia, um veiculo nesse caso precisa de um nome
nome2 = Nome('CG') 
nome_dono1 = Dono("Maicon") #Agregacao eh mais fraco, um veiculo nao necessariamente precisa de um dono
Carro1 = Carro(nome1, nome_dono1, 'Ford')
Moto1 = Moto(nome2, 'Micael', 'n lembro')
lista = [Carro1, Moto1]
# Polimorfismo
for i in range(2):
    print(andar(lista[i]))

soma = MathUtils.add(2,3) #Metodo estatico
print(soma) #Output: 5