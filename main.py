
from lib.funcionalidades import *
from lib.interface import *

minhas_tarefas = carregar_dados()

while True:
    print("""
==== MENU ====
1 - Adicionar
2 - Listar
3 - Remover
4 - Concluir
0 - Sair
""")

    op =leiaInt("Opção: ")

    if op == 1:
        adionar_tarefa()
    if op == 2:
        listar_tarefas(minhas_tarefas)
    else:
        break