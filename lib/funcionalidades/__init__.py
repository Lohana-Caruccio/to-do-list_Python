from lib.arquivo import *
from lib.interface import *
from datetime import datetime

def gerar_id(dados):
    if not dados:
        return 1
    else:
        return dados[-1]["id"] + 1

def adionar_tarefa():
    dados = carregar_dados()
    novo_id = gerar_id(dados)
    data_atual = datetime.now().strftime('%d/%m/%Y %H:%M')

    titulo = leiaStr('Nome da tarefa: ').upper()
    importancia = leiaInt('Importância de (1 a 5): ')

    nova_tarefa = {
        'id': novo_id,
        'titulo': titulo,
        'importancia': importancia,
        'status': 'Pendente',
        'criado_em': data_atual
    }
    dados.append(nova_tarefa)
    salvar_D(dados)
    print(f'Tarefa {titulo} adicionada com sucesso!')

def listar_tarefas(dados):
    if not dados:
       print( f'Sua lista de tarefas está vazia!')
       return

    print('\n' + '=' * 85)
    print(f"{'ID':<4} | {'TAREFA':<25} | {'PRIORIDADE':<10} | {'STATUS':<12} | {'CRIADO EM'}")
    print("-" * 85)

    for tarefa in dados:
        id_t = tarefa['id']
        titulo = tarefa['titulo']
        importancia = tarefa['importancia']
        status = tarefa['status']
        criado_em = tarefa['criado_em']

        estrelas = "*" * importancia

        print(f'{id_t:<4} | {titulo:<25} | {estrelas:<10} | {status:<12} | {criado_em}')

    print('=' * 85 + '\n')


