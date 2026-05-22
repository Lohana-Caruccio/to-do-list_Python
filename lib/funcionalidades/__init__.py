from lib.arquivo import *
from lib.interface import *
from datetime import datetime

def gerar_id(dados):
    if not dados:
        return 1
    else:
        return dados[-1]["id"] + 1


def adicionar_tarefa():
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
    print(f'<< Tarefa {titulo} adicionada com sucesso! >>')

def LISTAR():
    print('=' * 85)
    print('QUAIS TAREFAS VOCÊ DESEJA FILTRAR?')
    print('\n[1] PENDENTES\n'
          '[2] CONCLUÍDAS\n'
          '[3] TODAS')
    linha()


def listar_tarefas(dados):
    if not dados:
       print( f'Sua lista de tarefas está vazia!'.center(85))
       return

    print('\n' + '=' * 85)
    print(f"{'ID':<4} | {'TAREFA':<25} | {'PRIORIDADE':<10} | {'STATUS':<12} | {'CRIADO EM'}")
    print("=" * 85)

    for tarefa in dados:
        id_t = tarefa['id']
        titulo = tarefa['titulo']
        importancia = tarefa['importancia']
        status = tarefa['status']
        criado_em = tarefa['criado_em']

        estrelas = "*" * importancia

        print(f'{id_t:<4} | {titulo:<25} | {estrelas:<10} | {status:<12} | {criado_em}')
        print('-'*85)

    print('=' * 85 + '\n')


def filtrar_concluidas(dados):
    tarefas_concluidas = [t for t in dados if t['status'] == 'Concluída']
    cabecalho('TAREFAS CONCLUÍDAS')
    listar_tarefas(tarefas_concluidas)

def filtrar_pendentes(dados):
    tarefas_pendentes = [t for t in dados if t['status'] == 'Pendente']
    cabecalho('TAREFAS PENDENTES')
    listar_tarefas(tarefas_pendentes)


def remover_tarefas(dados):
    remover_id = leiaInt('\nID que deseja remover: ')
    dados_atualizados = [t for t in dados if t['id'] != remover_id]
    if len(dados_atualizados) == len(dados):
        print('ID não encontrado!')
        return
    salvar_D(dados_atualizados)
    dados[:] = dados_atualizados
    print('<< Tarefa removida com sucesso! >>')


def concluir_tarefa(dados):
    concluir_id = leiaInt('\nID que deseja concluir: ')
    encontrado = False

    for t in dados:
        if t['id'] == concluir_id:
            t['status'] = 'Concluída'
            encontrado = True
            break
    if not encontrado:
        print('ID não encontrado!')

    salvar_D(dados)
    print('<< Status da tarefa alterado para: Concluída >>')


def volta_pendencia(dados):
    pendente_id = leiaInt('\nID que deseja alterar para pendente: ')
    encontrado = False

    for t in dados:
        if t['id'] == pendente_id:
            t['status'] = 'Pendente'
            encontrado = True
            break
    if not encontrado:
        print('ID não encontrado!')

    salvar_D(dados)
    print('<< Status da tarefa alterado para: Pendente >>')


def editar_D(dados):
    print('-' * 85)
    print('ESCOLHA:')
    print('\n[1] REMOVER TAREFAS\n'
            '[2] MUDAR STATUS PARA CONCLUÍDA\n'
            '[3] MUDAR STATUS PARA PENDENTE\n')
    resp = leiaInt('Escolha uma opção: ')

    if resp == 1:
        remover_tarefas(dados)
    elif resp == 2:
        concluir_tarefa(dados)
    elif resp == 3:
        volta_pendencia(dados)
    else:
        print('\033[31mERRO: Digite uma opção válida!\033[m')