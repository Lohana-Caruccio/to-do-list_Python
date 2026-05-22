#SISTEMA DE TAREFAS
from lib.funcionalidades import *
from lib.interface import *

minhas_tarefas = carregar_dados()

while True:
    cabecalho('SISTEMA DE TAREFAS')
    print('MENU\n'.center(85))
    print('1 - ADICIONAR\n'
         '2 - LISTAR\n'
         '3 - EDITAR\n'
         '0 - SAIR\n')

    op =leiaInt("Opção: ")

    if op == 1:
        adicionar_tarefa()
        minhas_tarefas = carregar_dados()
    elif op == 2:
        LISTAR()
        resp = leiaInt('\nEscolha uma opção: ')
        if resp == 1:
            filtrar_pendentes(minhas_tarefas)
        elif resp == 2:
            filtrar_concluidas(minhas_tarefas)
        elif resp == 3:
            listar_tarefas(minhas_tarefas)
    elif op == 3:
        editar_D(minhas_tarefas)
        minhas_tarefas = carregar_dados()
    else:
        break

cabecalho('SESSÃO FINALIZADA!')