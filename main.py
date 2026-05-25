#SISTEMA DE TAREFAS
from lib.funcionalidades import *
from lib.interface import *

minhas_tarefas = carregar_dados()

while True:
    cabecalho('🩷 SISTEMA DE TAREFAS 🩷')
    print(colorir('💌 MENU 💌\n', 7).center(96))
    print('1 - ADICIONAR\n'
         '2 - LISTAR\n'
         '3 - EDITAR\n'
         '0 - SAIR\n')

    op =leiaInt("Opção: ")

    if op == 1:
        adicionar_tarefa()
        minhas_tarefas = carregar_dados()
    elif op == 2:
        while True:
            LISTAR()
            resp = leiaInt('\nEscolha uma opção: ')
            if resp == 1:
                filtrar_pendentes(minhas_tarefas)
            elif resp == 2:
                filtrar_concluidas(minhas_tarefas)
            elif resp == 3:
                cabecalho('TAREFAS')
                listar_tarefas(minhas_tarefas)
            elif resp == 0:
                break
            else:
                print(colorir('ERRO: Escolha uma opção válida. ', 1))
    elif op == 3:
        editar_D(minhas_tarefas)
        minhas_tarefas = carregar_dados()
    else:
        break

cabecalho('🩷 SESSÃO FINALIZADA! 🩷')