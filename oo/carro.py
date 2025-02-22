

"""
Você deve criar uma classe carro que vai possuir
dois  atributos compostos por outras duas classes:
1) motor e
2 direcao

O motor tera a responsabilidade de controlar a velocidade.
Ele oferecerá os seguintes atributos
1) Atributo de dado velocidade
2) Método acelerar que incrementara a velocidade em 1 unidade.
3) Método frear que decrementara a velocidade em 2 unidades.
A direção controlara a direção. Ela oferecera os seguintes atributos:
1) Valor de direção com os valores possivéis: norte, sul, leste, oeste
2) Girar a direita
3) Girar a esquerda
      N
    O   L
      S
      Exemplo
>>> motor = Motor()
>>> motor.velocidade
0
>>> motor.acelerar()
>>> motor.velocidade
1
>>> motor.acelerar()
>>> motor.velocidade
2
>>> motor.acelerar()
>>> motor.velocidade
3
>>> motor.frear()
>>> motor.velocidade
1
>>> motor.frear()
>>> motor.velocidade
0

 Teste direção

>>> direcao = Direcao()
>>> direcao.valor
'Norte'
>>> direcao.girar_a_direita()
>>> direcao.valor
'Leste'
>>> direcao.girar_a_direita()
>>> direcao.valor
'Sul'
>>> direcao.girar_a_direita()
>>> direcao.valor
'Oeste'
>>> direcao.girar_a_direita()
>>> direcao.valor
'Norte'
>>> direcao.girar_a_esquerda()
>>> direcao.valor
'Oeste'
>>> direcao.girar_a_esquerda()
>>> direcao.valor
'Sul'
>>> direcao.girar_a_esquerda()
>>> direcao.valor
'Leste'
>>> direcao.girar_a_esquerda()
>>> direcao.valor
'Norte'
>>> carro = Carro(direcao,motor)
>>> carro.calcular_velocidade()
0
>>> carro.acelerar()
>>> carro.calcular_velocidade()
1
>>> carro.acelerar()
>>> carro.calcular_velocidade()
2
>>> carro.frear()
>>> carro.calcular_velocidade()
0
>>> carro.calcular_direcao()
'Norte'
>>> carro.girar_a_direita()
>>> carro.calcular_direcao()
'Leste'
>>> carro.girar_a_esquerda()
>>> carro.calcular_direcao()
'Norte'
>>> carro.girar_a_esquerda()
>>> carro.calcular_direcao()
'Oeste'

"""
class Carro:
    def __init__(self, direcao, motor):
        self.motor = motor
        self.direcao = direcao

    def calcular_velocidade(self):
        return(self.motor.velocidade)

    def acelerar(self):
        self.motor.acelerar()

    def frear(self):
        self.motor.frear()

    def calcular_direcao(self):
        return(self.direcao.valor)

    def girar_a_direita(self):
        self.direcao.girar_a_direita()

    def girar_a_esquerda(self):
        self.direcao.girar_a_esquerda()

class Motor():

    def __init__(self):
        self.velocidade = 0

    def acelerar(self):
        self.velocidade += 1

    def frear(self):
        self.velocidade = max(0, self.velocidade - 2)
        #self.velocidade -= 2
        #if self.velocidade < 0:
        #    self.velocidade = 0

NORTE = 'Norte'
SUL = 'Sul'
LESTE = 'Leste'
OESTE = 'Oeste'

class Direcao:
    rotacao_direita_dct = {NORTE: LESTE, LESTE: SUL, SUL: OESTE, OESTE: NORTE}
    rotacao_esquerda_dct = {NORTE: OESTE, OESTE: SUL, SUL: LESTE, LESTE: NORTE }
    def __init__(self):
        self.valor = NORTE

    def girar_a_direita(self):
        self.valor = self.rotacao_direita_dct[self.valor]

    def girar_a_esquerda(self):
        self.valor = self.rotacao_esquerda_dct[self.valor]
