import json
import os

DOC_DADOS = 'tarefas.json'

def carregar_dados():
    if not os.path.exists(DOC_DADOS):
        return []
    try:
        with open(DOC_DADOS, 'r', encoding='utf-8') as documentos:
            return json.load(documentos)
    except (json.JSONDecoder, FileNotFoundError):
        return []


def salvar_D(lista_dados):
    try:
        with open(DOC_DADOS, 'w', encoding='utf-8') as documentos:
            json.dump(lista_dados, documentos, indent=4, ensure_ascii=False)
        return True
    except (OSError, TypeError):
        print('\033[31mERRO: Não foi possível salvar as alterações na sua lista de tarefas.\033[m')
        return False
    