from lib.interface import *
def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print(colorir('ERRO: Por favor digite um número inteiro válido.',1))
        except KeyboardInterrupt:
            print(colorir('ERRO: Entrada de dados intemrrompida pelo usuário.',1))
            return 0
        else:
            break
    return n

def leiaStr(msg):
    while True:
        try:
            t = str(input(msg))
        except (ValueError, TypeError):
            print(colorir('ERRO: Por favor digite uma mensagem válida.', 1))
        except KeyboardInterrupt:
            print(colorir('ERRO: Entrada de dados intemrrompida pelo usuário.', 1))
            return 0
        else:
            break
    return t

def linha(tam=85):
    return '-' * tam

def cabecalho(txt):
    print(linha())
    emojis = ['🩷']
    extra = sum(txt.count(e) for e in emojis)
    tamanho_ajustado = 85 - extra
    texto_centralizado = txt.center(tamanho_ajustado)
    print(colorir(texto_centralizado, i=8))
    print(linha())


#Tupla para guardar as cores
c = ('\033[0m',    #0 -sem cores
    '\033[0;31m', #1- vermelho
    '\033[0;32m', #2 - verde
    '\033[0;33m', #3 -amarelo
    '\033[0;34m', #4 - azul
    '\033[0;35m', #5 - roxo
    '\033[0;36m',  #6 - azul piscina
    '\033[4;35m', # 7 - roxo sublinhado
    '\033[0;35;107m' #8 - roxo com fundo branco
     )

def colorir(txt=0, i=0):
    cor_escolhida = c[i]
    reset = c[0]
    return f'{cor_escolhida}{txt}{reset}'