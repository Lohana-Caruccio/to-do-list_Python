
def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print(f'\033[31mERRO: Por favor digite um número inteiro válido.\033[m')
        except KeyboardInterrupt:
            print(f'\n\33[31mERRO: Entrada de dados intemrrompida pelo usuário.\033[m')
            return 0
        else:
            break
    return n

def leiaStr(msg):
    while True:
        try:
            t = str(input(msg))
        except (ValueError, TypeError):
            print(f'\033[31mERRO: Por favor digite uma mensagem válida.\033[m')
        except KeyboardInterrupt:
            print(f'\n\33[31mERRO: Entrada de dados intemrrompida pelo usuário.\033[m')
            return 0
        else:
            break
    return t

def linha(tam=85):
    return '-' * tam

def cabecalho(txt):
    print(linha())
    print(txt.center(85))
    print(linha())
