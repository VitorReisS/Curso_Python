# Métodos em instâncias de classes Python
# Hard coded - É algo que foi escrito diretamente no código

class Carro:
    def __init__(self, nome):
        self.nome = nome

    def acelerar(self):
        print(f'{self.nome} está acelerando...')

string = 'Vitor'
print(string.upper())

fusca = Carro('Fusca')
print(fusca.nome)
fusca.acelerar()

voyage = Carro(nome='voyage')
print(voyage.nome)
voyage.acelerar()