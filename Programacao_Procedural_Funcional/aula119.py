# Exercício - Lista de tarefas com desfazer e refazer
# Música para codar =)
# Everybody wants to rule the world - Tears for fears
# todo = [] -> lista de tarefas
# todo = ['fazer café'] -> Adicionar fazer café
# todo = ['fazer café', 'caminhar'] -> Adicionar caminhar
# desfazer = ['fazer café',] -> Refazer ['caminhar']
# desfazer = [] -> Refazer ['caminhar', 'fazer café']
# refazer = todo ['fazer café']
# refazer = todo ['fazer café', 'caminhar']

import os

def listar(tarefas):
    if not tarefas:
        print()
        print('Nenhuma tarefa para listar')
        print()
        return

    print('Tarefas:')
    for tarefa in tarefas:
        print(f'\t{tarefa}')
    print()

def desfazer(tarefas, tarefas_refazer):
    if not tarefas:
        print()
        print('Nenhuma tarefa para desfazer')
        print()
        return
    
    tarefa = tarefas.pop()
    print()
    print(f'{tarefa=} removida da lista de tarefas.')
    tarefas_refazer.append(tarefa)
    print()
    listar(tarefas)

def refazer(tarefa, tarefas_refazer):
    if not tarefas_refazer:
        print()
        print('Nenhuma tarefa para refazer')
        print()
        return

    tarefa = tarefas_refazer.pop()
    print()
    print(f'{tarefa=} adicionada na lista de tarefas.')
    tarefas.append(tarefa)
    print()
    listar(tarefas)

def adicionar(tarefa, tarefas):
    tarefa = tarefa.strip()
    if not tarefa:
        print()
        print('Você não digitou uma tarefa.')
        print()
        return
    
    print()
    print(f'{tarefa=} adicionada na lista de tarefas.')
    tarefas.append(tarefa)
    print()
    listar(tarefas)

tarefas = []
tarefas_refazer = []

while True:
    print('Comandos: listar, desfazer e refazer')
    tarefa = input('Digite uma tarefa ou comando: ')

    comandos = {
        'listar': lambda: listar(tarefas),
        'desfazer': lambda: desfazer(tarefas, tarefas_refazer),
        'refazer': lambda: refazer(tarefas, tarefas_refazer),
        'clear': lambda: os.system('cls'),
        'adicionar': lambda: adicionar(tarefa, tarefas),
    }

    comando = comandos.get(tarefa) if comandos.get(tarefa) is not None else comandos['adicionar']
    comando()

    # if tarefa == 'listar':
    #     listar(tarefas)
    #     continue
    # elif tarefa == 'desfazer':
    #     desfazer(tarefas, tarefas_refazer)
    #     listar(tarefas)
    #     continue
    # elif tarefa == 'refazer':
    #     refazer(tarefas, tarefas_refazer)
    #     listar(tarefas)
    #     continue
    # elif tarefa == '0':
    #     break
    # elif tarefa == 'clear':
    #     os.system('cls')
    #     continue
    # else:
    #     adicionar(tarefa, tarefas)
    #     listar(tarefas)
    #     continue