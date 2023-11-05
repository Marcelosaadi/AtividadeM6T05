##criando classe animal
class animal:
    animais = []
    def __init__(self,nome,especie,felicidade):
        self.nome=nome
        self.especie=especie
        self.felicidade=felicidade
        self.animais.append(self)
    def alimentar(self, comidinha):
        self.felicidade = self.felicidade + comidinha

##criando classe recintos
class recinto:
    recintos= []
    def __init__(self, nome, especie, cuidado):
        self.nome = nome
        self.especie = especie
        self.animais = []
        self.cuidado = cuidado
        self.recintos.append(self)

##criando função para adicionar animal
    def adicionar_animal(self, animal):
        if animal.especie == self.especie:
            self.animais.append(animal)
            #checando se é da mesma espécie
            print(f'{animal.nome} animal adicionado com sucesso' )
        else:
            print(f'{animal.nome} não é da mesma espécie')
    
    ##criando função para aumentar o cuidado do habitat
    def aumentar_cuidado(self, nota):
        self.cuidado = self.cuidado + nota

##criando classe jgoador
class jogador:
    def __init__(self, nome, dinheiros):
        self.dinheiros = dinheiros
        self.nome = nome
    
    #criando função para o usuário receber mais dinheiro caso os animais estejam felizes e os habitats bem cuidados
    def receberDinheiros(self, ganhouDinheiros):
        self.dinheiros = self.dinheiros + ganhouDinheiros




#criando o jogador
jogador1 = jogador('MateusDoMalReiDasCocotas12345', 0)    

#criando habitat da tundra
habitat_tundra = recinto('tundra', 'zebra', 80)

#criando zebras
zebra_joaquim =animal('joaquim', 'zebra', 10)
zebra_marcelo =animal('marcelo', 'zebra', 50)

#criando lagarto
lagarto_brita = animal('brita', 'lagarto', 20)


#adicionando nos habitats
habitat_tundra.adicionar_animal(zebra_joaquim)

#forçando o erro ao adicionar o lagarto brita
habitat_tundra.adicionar_animal(lagarto_brita)

#printando o cuidado do habitat
print(f'{habitat_tundra.cuidado} o recinto tem esse cuidado atualmente')
#aumentando o cuidado do habitat
habitat_tundra.aumentar_cuidado(20)
print(f'{habitat_tundra.cuidado}')
#mostrando a felicidade da zebra joaquim
print(f'joaquim está triste: {zebra_joaquim.felicidade}')
#alimentando joaquim para deixa-lo feliz
zebra_joaquim.alimentar(50)
#joaquim ficou feliz
print(f'joaquim está muito feliz agora que você alimentou ele: {zebra_joaquim.felicidade}')

#criando for para calcular a quantidade de dinheiro que o usuário estará disposto a gastar no zoologico com base no cuidado dos recintos e na felicidade dos animais
soma = 0
for recinto in recinto.recintos:
    soma = soma+ recinto.cuidado

for wrar in animal.animais:
    soma = soma+wrar.felicidade



dinheiros = soma/2
jogador1.receberDinheiros(dinheiros)
print(jogador1.dinheiros)
print(soma)



##realizei os testes com os prints, tentei utilizar bibliotecas no python para testar mas realmente não estava conseguindo