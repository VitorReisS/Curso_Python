# class - Classes são moldes para criar novos objetos
# Introdução ao método __init__ (inicializador de atributos)
# As classes geram novos objetos (instâncias) que
# podem ter seus próprios atributos e métodos.
# Os objetos gerados pela classe podem usar seus dados
# internos para realizar várias ações.
# Por convenção, usamos PascalCase para nomes de
# classes.

# string = 'Vitor'  # str
# print(string.upper())
# print(isinstance(string, str))

class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome


p1 = Pessoa('Vitor', 'Reis')
# p1.nome = 'Vitor'
# p1.sobrenome = 'Reis'

p2 = Pessoa('Maria', 'Joana')
# p2.nome = 'Maria'
# p2.sobrenome = 'Joana'

print(p1.nome)
print(p1.sobrenome)

print(p2.nome)
print(p2.sobrenome)